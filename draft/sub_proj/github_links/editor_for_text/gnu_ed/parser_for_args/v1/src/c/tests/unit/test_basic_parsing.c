/* Unit tests for Basic Parsing requirement (001_requi_basic_parsing.md) */
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "carg_parser.h"

static int test_short_options(void) {
    printf("Test: short options parsing\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'a', 0, ap_no},
        {'b', 0, ap_no},
        {'c', 0, ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-a", "-b", "-c", 0};
    char result = ap_init(&ap, 4, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 3);
    assert(ap_code(&ap, 0) == 'a');
    assert(ap_code(&ap, 1) == 'b');
    assert(ap_code(&ap, 2) == 'c');
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_combined_short_options(void) {
    printf("Test: combined short options (-abc)\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'a', 0, ap_no},
        {'b', 0, ap_no},
        {'c', 0, ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-abc", 0};
    char result = ap_init(&ap, 2, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 3);
    assert(ap_code(&ap, 0) == 'a');
    assert(ap_code(&ap, 1) == 'b');
    assert(ap_code(&ap, 2) == 'c');
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_long_options(void) {
    printf("Test: long options parsing\n");
    Arg_parser ap;
    ap_Option options[] = {
        {0, "verbose", ap_no},
        {0, "output", ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "--verbose", "--output=file.txt", 0};
    char result = ap_init(&ap, 3, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 2);
    assert(strcmp(ap_parsed_name(&ap, 0), "--verbose") == 0);
    assert(strcmp(ap_parsed_name(&ap, 1), "--output") == 0);
    assert(strcmp(ap_argument(&ap, 1), "file.txt") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_non_option_args(void) {
    printf("Test: non-option arguments\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'f', 0, ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "file1.txt", "-f", "file2.txt", 0};
    char result = ap_init(&ap, 5, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 3);
    assert(ap_code(&ap, 0) == 0);  /* non-option */
    assert(ap_code(&ap, 1) == 'f');
    assert(ap_code(&ap, 2) == 0);  /* non-option */
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Basic Parsing Unit Tests ===\n");
    test_short_options();
    test_combined_short_options();
    test_long_options();
    test_non_option_args();
    printf("All basic parsing tests PASSED\n");
    return 0;
}
