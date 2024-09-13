---
title: instance_details
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_details
  - osconfig
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

Creates, updates, deletes, gets or lists a <code>instance_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.osconfig.instance_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The instance name in the form `projects/*/zones/*/instances/*` |
| <CopyableCode code="attemptCount" /> | `string` | The number of times the agent that the agent attempts to apply the patch. |
| <CopyableCode code="failureReason" /> | `string` | If the patch fails, this field provides the reason. |
| <CopyableCode code="instanceSystemId" /> | `string` | The unique identifier for the instance. This identifier is defined by the server. |
| <CopyableCode code="state" /> | `string` | Current state of instance patch. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="patchJobsId, projectsId" /> | Get a list of instance details for a given patch job. |

## `SELECT` examples

Get a list of instance details for a given patch job.

```sql
SELECT
name,
attemptCount,
failureReason,
instanceSystemId,
state
FROM google.osconfig.instance_details
WHERE patchJobsId = '{{ patchJobsId }}'
AND projectsId = '{{ projectsId }}'; 
```
