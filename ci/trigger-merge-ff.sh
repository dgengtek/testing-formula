#!/usr/bin/env bash
readonly concourse_pipeline="salt-formulas-testing"
fly -t local trigger-job -j "$concourse_pipeline/j-merge-ff"
