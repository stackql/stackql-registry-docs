---
title: nas_trial_details
hide_title: false
hide_table_of_contents: false
keywords:
  - nas_trial_details
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

Creates, updates, deletes or gets an <code>nas_trial_detail</code> resource or lists <code>nas_trial_details</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nas_trial_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.nas_trial_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the NasTrialDetail. |
| <CopyableCode code="parameters" /> | `string` | The parameters for the NasJob NasTrial. |
| <CopyableCode code="searchTrial" /> | `object` | Represents a uCAIP NasJob trial. |
| <CopyableCode code="trainTrial" /> | `object` | Represents a uCAIP NasJob trial. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, nasJobsId, nasTrialDetailsId, projectsId" /> | Gets a NasTrialDetail. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, nasJobsId, projectsId" /> | List top NasTrialDetails of a NasJob. |

## `SELECT` examples

List top NasTrialDetails of a NasJob.

```sql
SELECT
name,
parameters,
searchTrial,
trainTrial
FROM google.aiplatform.nas_trial_details
WHERE locationsId = '{{ locationsId }}'
AND nasJobsId = '{{ nasJobsId }}'
AND projectsId = '{{ projectsId }}'; 
```
