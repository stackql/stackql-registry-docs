---
title: results
hide_title: false
hide_table_of_contents: false
keywords:
  - results
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

Creates, updates, deletes or gets an <code>result</code> resource or lists <code>results</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the test case result. Format: `projects//locations//agents//testCases//results/`. |
| <CopyableCode code="conversationTurns" /> | `array` | The conversation turns uttered during the test case replay in chronological order. |
| <CopyableCode code="environment" /> | `string` | Environment where the test was run. If not set, it indicates the draft environment. |
| <CopyableCode code="testResult" /> | `string` | Whether the test case passed in the agent environment. |
| <CopyableCode code="testTime" /> | `string` | The time that the test was run. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_test_cases_results_get" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId, resultsId, testCasesId" /> | Gets a test case result. |
| <CopyableCode code="projects_locations_agents_test_cases_results_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId, testCasesId" /> | Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case. |

## `SELECT` examples

Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case.

```sql
SELECT
name,
conversationTurns,
environment,
testResult,
testTime
FROM google.dialogflow.results
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND testCasesId = '{{ testCasesId }}'; 
```
