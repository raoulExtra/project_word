/* Unit tests for Option Arguments requirement (020_requi_option_arguments.md) */
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "carg_parser.h"

static int test_required_argument(void) {
    printf("Test: required argument\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'o', 0, ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-o", "value", 0};
    char result = ap_init(&ap, 3, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 1);
    assert(ap_code(&ap, 0) == 'o');
    assert(strcmp(ap_argument(&ap, 0), "value") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_optional_argument(void) {
    printf("Test: optional argument\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'d', 0, ap_maybe},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-d", "value", 0};
    char result = ap_init(&ap, 3, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 1);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_long_option_with_equals(void) {
    printf("Test: long option with = syntax\n");
    Arg_parser ap;
    ap_Option options[] = {
        {0, "output", ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "--output=result.txt", 0};
    char result = ap_init(&ap, 2, argv, options, 0);
    assert(result != 0);
    assert(strcmp(ap_argument(&ap, 0), "result.txt") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_no_argument_option(void) {
    printf("Test: option with no argument\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'v', 0, ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-v", 0};
    char result = ap_init(&ap, 2, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 1);
    assert(ap_code(&ap, 0) == 'v');
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Option Arguments Unit Tests ===\n");
    test_required_argument();
    test_optional_argument();
    test_long_option_with_equals();
    test_no_argument_option();
    printf("All option argument tests PASSED\n");
    return 0;
}
