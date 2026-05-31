/* Unit tests for Long Option Matching requirement (040_requi_long_option_matching.md) */
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "carg_parser.h"

static int test_exact_match(void) {
    printf("Test: exact long option match\n");
    Arg_parser ap;
    ap_Option options[] = {
        {0, "verbose", ap_no},
        {0, "output", ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "--verbose", "--output", 0};
    char result = ap_init(&ap, 3, argv, options, 0);
    assert(result != 0);
    assert(strcmp(ap_parsed_name(&ap, 0), "--verbose") == 0);
    assert(strcmp(ap_parsed_name(&ap, 1), "--output") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_abbreviated_match(void) {
    printf("Test: abbreviated long option\n");
    Arg_parser ap;
    ap_Option options[] = {
        {0, "verbose", ap_no},
        {0, "version", ap_no},
        {0, "very", ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "--verb", 0};  /* unambiguous abbreviation */
    char result = ap_init(&ap, 2, argv, options, 0);
    assert(result != 0);
    assert(strcmp(ap_parsed_name(&ap, 0), "--verbose") == 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

static int test_ambiguous_option(void) {
    printf("Test: ambiguous long option\n");
    Arg_parser ap;
    ap_Option options[] = {
        {0, "verbose", ap_no},
        {0, "version", ap_no},
        {0, 0, ap_no}
    };
    const char *argv[] = {"prog", "--ver", 0};  /* ambiguous: matches both */
    ap_init(&ap, 2, argv, options, 0);
    assert(ap_error(&ap) != 0);
    assert(strstr(ap_error(&ap), "ambiguous") != 0);
    ap_free(&ap);
    printf("  PASSED\n");
    return 0;
}

int main(void) {
    printf("=== Long Option Matching Unit Tests ===\n");
    test_exact_match();
    test_abbreviated_match();
    test_ambiguous_option();
    printf("All long option matching tests PASSED\n");
    return 0;
}
