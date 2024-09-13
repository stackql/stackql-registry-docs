
---
title: trials_optimal_trials
hide_title: false
hide_table_of_contents: false
keywords:
  - trials_optimal_trials
  - aiplatform
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

Creates, updates, deletes or gets an <code>trials_optimal_trial</code> resource or lists <code>trials_optimal_trials</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trials_optimal_trials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.trials_optimal_trials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="optimalTrials" /> | `array` | The pareto-optimal Trials for multiple objective Study or the optimal trial for single objective Study. The definition of pareto-optimal can be checked in wiki page. https://en.wikipedia.org/wiki/Pareto_efficiency |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_optimal_trials" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Lists the pareto-optimal Trials for multi-objective Study or the optimal Trials for single-objective Study. The definition of pareto-optimal can be checked in wiki page. https://en.wikipedia.org/wiki/Pareto_efficiency |

## `SELECT` examples

Lists the pareto-optimal Trials for multi-objective Study or the optimal Trials for single-objective Study. The definition of pareto-optimal can be checked in wiki page. https://en.wikipedia.org/wiki/Pareto_efficiency

```sql
SELECT
optimalTrials
FROM google.aiplatform.trials_optimal_trials
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND studiesId = '{{ studiesId }}'; 
```
