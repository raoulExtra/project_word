/* Unit tests for Duplicate Options requirement (110_requi_duplicate_options.md) */
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "carg_parser.h"

static int test_repeated_short_options(void) {
    printf("Test: repeated short options (last wins)\n");
    Arg_parser ap;
    ap_Option options[] = {
        {'v', 0, ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "-v", "first", "-v", "second", 0};
    char result = ap_init(&ap, 5, argv, options, 0);
    assert(result != 0);
    assert(ap_arguments(&ap) == 4);
    /* Both occurrences are recorded, last value is "second" */
    assert(ap_code(&ap, 0) == 'v');
    assert(ap_code(&ap, 2) == 'v');
    assert(strcmp(ap_argument(&ap, 1), "first") == 0);
    assert(strcmp(ap_argument(&ap, 3), "second") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_repeated_long_options(void) {
    printf("Test: repeated long options\n");
    Arg_parser ap;
    ap_Option options[] = {
        {0, "count", ap_yes},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "--count=1", "--count=5", 0};
    char result = ap_init(&ap, 4, argv, options, 0);
    assert(result != 0);
    assert(strcmp(ap_argument(&ap, 0), "1") == 0);
    assert(strcmp(ap_argument(&ap, 1), "5") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Duplicate Options Unit Tests ===\n");
    test_repeated_short_options();
    test_repeated_long_options();
    printf("All duplicate option tests PASSED\n");
    return 0;
}
