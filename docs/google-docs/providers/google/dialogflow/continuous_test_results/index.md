---
title: continuous_test_results
hide_title: false
hide_table_of_contents: false
keywords:
  - continuous_test_results
  - dialogflow
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>continuous_test_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>continuous_test_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.continuous_test_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the continuous test result. Format: `projects//locations//agents//environments//continuousTestResults/`. |
| <CopyableCode code="result" /> | `string` | The result of this continuous test run, i.e. whether all the tests in this continuous test run pass or not. |
| <CopyableCode code="runTime" /> | `string` | Time when the continuous testing run starts. |
| <CopyableCode code="testCaseResults" /> | `array` | A list of individual test case results names in this continuous test run. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_environments_continuous_test_results_list" /> | `SELECT` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Fetches a list of continuous test results for a given environment. |

## `SELECT` examples

Fetches a list of continuous test results for a given environment.

```sql
SELECT
name,
result,
runTime,
testCaseResults
FROM google.dialogflow.continuous_test_results
WHERE agentsId = '{{ agentsId }}'
AND environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
