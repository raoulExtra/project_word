/* Unit tests for Error Handling requirement (030_requi_error_handling.md) */
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "carg_parser.h"

static int test_unrecognized_option(void) {
    printf("Test: unrecognized option\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'a', 0, ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-z", 0};
    ap_init(&ap, 2, argv, options, 0);
    assert(ap_error(&ap) != 0);
    assert(strstr(ap_error(&ap), "unrecognized") != 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_missing_required_argument(void) {
    printf("Test: missing required argument\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'o', 0, ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-o", 0};  /* missing argument */
    ap_init(&ap, 2, argv, options, 0);
    assert(ap_error(&ap) != 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_invalid_option(void) {
    printf("Test: invalid option character\n");
    Arg_parser ap;
    ap_Option options[] = {{0, 0, ap_no}};
    const char *argv[] = {"prog", "--invalid", 0};
    ap_init(&ap, 2, argv, options, 0);
    assert(ap_error(&ap) != 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Error Handling Unit Tests ===\n");
    test_unrecognized_option();
    test_missing_required_argument();
    test_invalid_option();
    printf("All error handling tests PASSED\n");
    return 0;
}
