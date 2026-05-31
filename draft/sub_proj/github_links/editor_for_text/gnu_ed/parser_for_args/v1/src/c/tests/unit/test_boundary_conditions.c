/* Unit tests for Boundary Conditions requirement (080_requi_boundary_conditions.md) */
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "carg_parser.h"

static int test_zero_arguments(void) {
    printf("Test: zero arguments (argc=1)\n");
    Arg_parser ap;
    ap_Option options[] = {{0, 0, ap_no}};
    const char *argv[] = {"prog", 0};
    char result = ap_init(&ap, 1, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_invalid_index(void) {
    printf("Test: invalid index in accessors\n");
    Arg_parser ap;
    ap_Option options[] = {{0, 0, ap_no}};
    const char *argv[] = {"prog", 0};
    ap_init(&ap, 1, argv, options, 0);
    
    /* Should return 0 for invalid indices */
    assert(ap_code(&ap, -1) == 0);
    assert(ap_code(&ap, 100) == 0);
    assert(strcmp(ap_argument(&ap, -1), "") == 0);
    assert(strcmp(ap_argument(&ap, 100), "") == 0);
    assert(strcmp(ap_parsed_name(&ap, -1), "") == 0);
    
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_null_option_array(void) {
    printf("Test: null options array\n");
    Arg_parser ap;
    const char *argv[] = {"prog", 0};
    char result = ap_init(&ap, 1, argv, NULL, 0);
    assert(result != 0);  /* Should succeed (return 1) */
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Boundary Conditions Unit Tests ===\n");
    test_zero_arguments();
    test_invalid_index();
    test_null_option_array();
    printf("All boundary condition tests PASSED\n");
    return 0;
}
