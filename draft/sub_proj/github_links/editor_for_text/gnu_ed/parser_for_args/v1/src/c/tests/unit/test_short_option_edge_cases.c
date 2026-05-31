/* Unit tests for Short Option Edge Cases requirement (090_requi_short_option_edge_cases.md) */
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "carg_parser.h"

static int test_combined_with_attached_argument(void) {
    printf("Test: combined short options with attached argument\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'a', 0, ap_no},
        {'b', 0, ap_no},
        {'c', 0, ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-abcvalue", 0};
    char result = ap_init(&ap, 2, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 3);
    assert(ap_code(&ap, 0) == 'a');
    assert(ap_code(&ap, 1) == 'b');
    assert(ap_code(&ap, 2) == 'c');
    assert(strcmp(ap_argument(&ap, 2), "value") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_single_with_attached_argument(void) {
    printf("Test: single option with attached argument\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'f', 0, ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-ffile.txt", 0};
    char result = ap_init(&ap, 2, argv, options, 0);
    assert(result != 0);
    assert(strcmp(ap_argument(&ap, 0), "file.txt") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_combined_with_separate_argument(void) {
    printf("Test: combined options with separate argument\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'a', 0, ap_no},
        {'b', 0, ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-ab", "value", 0};
    char result = ap_init(&ap, 3, argv, options, 0);
    assert(result != 0);
    assert(ap_code(&ap, 0) == 'a');
    assert(ap_code(&ap, 1) == 'b');
    assert(strcmp(ap_argument(&ap, 1), "value") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Short Option Edge Cases Unit Tests ===\n");
    test_combined_with_attached_argument();
    test_single_with_attached_argument();
    test_combined_with_separate_argument();
    printf("All short option edge case tests PASSED\n");
    return 0;
}
