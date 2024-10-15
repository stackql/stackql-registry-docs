---
title: job_runbook_contents
hide_title: false
hide_table_of_contents: false
keywords:
  - job_runbook_contents
  - automation
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

Creates, updates, deletes, gets or lists a <code>job_runbook_contents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_runbook_contents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.job_runbook_contents" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, jobName, resourceGroupName, subscriptionId" /> | Retrieve the runbook content of the job identified by job name. |

## `SELECT` examples

Retrieve the runbook content of the job identified by job name.


```sql
SELECT

FROM azure.automation.job_runbook_contents
WHERE automationAccountName = '{{ automationAccountName }}'
AND jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```