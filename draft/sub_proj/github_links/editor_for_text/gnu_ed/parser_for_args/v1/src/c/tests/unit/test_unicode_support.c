/* Unit tests for Unicode Support requirement (100_requi_unicode_support.md) */
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "carg_parser.h"

static int test_utf8_option_name(void) {
    printf("Test: UTF-8 in option name\n");
    Arg_parser ap;
    ap_Option options[] = {
        {0, "verbose", ap_no},
        {0, "café", ap_no},  /* UTF-8 option name */
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "--café", 0};
    char result = ap_init(&ap, 2, argv, options, 0);
    assert(result != 0);
    assert(strcmp(ap_parsed_name(&ap, 0), "--café") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_utf8_argument_value(void) {
    printf("Test: UTF-8 in argument value\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'n', 0, ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-n", "日本語", 0};  /* Japanese characters */
    char result = ap_init(&ap, 3, argv, options, 0);
    assert(result != 0);
    assert(strcmp(ap_argument(&ap, 0), "日本語") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Unicode Support Unit Tests ===\n");
    test_utf8_option_name();
    test_utf8_argument_value();
    printf("All unicode support tests PASSED\n");
    return 0;
}
