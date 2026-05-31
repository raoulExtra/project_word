/* Unit tests for Negative Numbers requirement (060_requi_negative_numbers.md) */
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "carg_parser.h"

static int test_negative_integer(void) {
    printf("Test: negative integer as argument\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'v', 0, ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-v", "-42", 0};
    char result = ap_init(&ap, 3, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 2);
    assert(ap_code(&ap, 0) == 'v');
    assert(ap_code(&ap, 1) == 0);  /* -42 as non-option */
    assert(strcmp(ap_argument(&ap, 1), "-42") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_negative_float(void) {
    printf("Test: negative float as argument\n");
    Arg_parser ap;
    ap_Option options[] = {
        {0, "value", ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "--value", "-3.14", 0};
    char result = ap_init(&ap, 3, argv, options, 0);
    assert(result != 0);
    assert(strcmp(ap_argument(&ap, 0), "-3.14") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Negative Numbers Unit Tests ===\n");
    test_negative_integer();
    test_negative_float();
    printf("All negative number tests PASSED\n");
    return 0;
}
