/* Unit tests for Empty Arguments requirement (070_requi_empty_arguments.md) */
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "carg_parser.h"

static int test_empty_string_argument(void) {
    printf("Test: empty string as argument\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'o', 0, ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-o", "", 0};
    char result = ap_init(&ap, 3, argv, options, 0);
    assert(result != 0);
    assert(strcmp(ap_argument(&ap, 0), "") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_empty_long_option_equals(void) {
    printf("Test: empty long option value\n");
    Arg_parser ap;
    ap_Option options[] = {
        {0, "output", ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "--output=", 0};
    char result = ap_init(&ap, 2, argv, options, 0);
    assert(result != 0);
    assert(strcmp(ap_argument(&ap, 0), "") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_standalone_dash_dash(void) {
    printf("Test: standalone -- terminates options\n");
    Arg_parser ap;
    ap_Option options[] = {{0, 0, ap_no}};
    const char *argv[] = {"prog", "--", "file", 0};
    char result = ap_init(&ap, 4, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 2);  /* "--" and "file" as non-options */
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Empty Arguments Unit Tests ===\n");
    test_empty_string_argument();
    test_empty_long_option_equals();
    test_standalone_dash_dash();
    printf("All empty argument tests PASSED\n");
    return 0;
}
