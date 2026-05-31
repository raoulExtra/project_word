/* Unit tests for Argument Order requirement (050_requi_argument_order.md) */
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "carg_parser.h"

static int test_default_order(void) {
    printf("Test: default argument order (options reordered)\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'a', 0, ap_no},
        {'b', 0, ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "file1", "-a", "file2", "-b", 0};
    char result = ap_init(&ap, 6, argv, options, 0);
    assert(result != 0);
    /* Options appear first, then non-options */
    assert(ap_code(&ap, 0) == 'a');
    assert(ap_code(&ap, 1) == 'b');
    assert(ap_code(&ap, 2) == 0);  /* non-option */
    assert(ap_code(&ap, 3) == 0);  /* non-option */
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_in_order(void) {
    printf("Test: preserve argument order\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'a', 0, ap_no},
        {'b', 0, ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "file1", "-a", "file2", "-b", 0};
    char result = ap_init(&ap, 6, argv, options, ap_in_order);
    assert(result != 0);
    /* Arguments should be in original order */
    assert(ap_code(&ap, 0) == 0);  /* file1 */
    assert(ap_code(&ap, 1) == 'a');
    assert(ap_code(&ap, 2) == 0);  /* file2 */
    assert(ap_code(&ap, 3) == 'b');
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_end_of_options_marker(void) {
    printf("Test: -- terminates options\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'a', 0, ap_no},
        {'b', 0, ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-a", "--", "-b", 0};
    char result = ap_init(&ap, 5, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 3);
    assert(ap_code(&ap, 0) == 'a');
    assert(ap_code(&ap, 1) == 0);  /* -b as non-option */
    assert(ap_code(&ap, 2) == 0);  /* end */
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Argument Order Unit Tests ===\n");
    test_default_order();
    test_in_order();
    test_end_of_options_marker();
    printf("All argument order tests PASSED\n");
    return 0;
}
