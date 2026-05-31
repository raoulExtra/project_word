/* Unit tests for Memory Management requirement (010_requi_memory_management.md) */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "carg_parser.h"

static int test_basic_allocation(void) {
    printf("Test: basic memory allocation\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'a', 0, ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-a", 0};
    char result = ap_init(&ap, 2, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 1);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_large_argument_count(void) {
    printf("Test: large argument count\n");
    Arg_parser ap;
    ap_Option options[] = {{0, 0, ap_no}};
    
    /* Build argv with many arguments */
    const int argc = 100;
    char *argv[101];
    char arg_buf[16];
    argv[0] = "prog";
    for(int i = 1; i < argc; i++) {
        sprintf(arg_buf, "arg%d", i);
        argv[i] = arg_buf;
    }
    
    char result = ap_init(&ap, argc, argv, options, ap_in_order);
    assert(result != 0);
    assert(ap_arguments(&ap) == argc - 1);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_error_message_allocation(void) {
    printf("Test: error message allocation\n");
    Arg_parser ap;
    ap_Option options[] = {{0, 0, ap_no}};
    const char *argv[] = {"prog", "-z", 0};  /* invalid option */
    
    ap_init(&ap, 2, argv, options, 0);
    assert(ap_error(&ap) != 0);  /* Should have error message */
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Memory Management Unit Tests ===\n");
    test_basic_allocation();
    test_large_argument_count();
    test_error_message_allocation();
    printf("All memory management tests PASSED\n");
    return 0;
}
