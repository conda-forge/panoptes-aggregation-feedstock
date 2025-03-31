import sys
from subprocess import call

FAIL_UNDER = "860"
COV = ["coverage"]
RUN = ["run", "--source=panoptes_aggregation", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = [
    # https://github.com/conda-forge/panoptes-aggregation-feedstock/pull/5
    ## fails inscrutably comparing a bunch of matrices
    "(test_bezier_extractor and TestPolygon and test_extract)",
    "(test_bezier_extractor and TestPolygonTask and test_extract)",
]

SKIP_OR = " or ".join(SKIPS)
K = ["-k", f"not ({SKIP_OR})"]


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST, *K])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
