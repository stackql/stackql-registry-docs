---
title: jobs_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_credentials
  - data_box
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

Creates, updates, deletes, gets or lists a <code>jobs_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box.jobs_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="jobName" /> | `string` | Name of the job. |
| <CopyableCode code="jobSecrets" /> | `object` | The base class for the secrets |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | This method gets the unencrypted secrets related to the job. |

## `SELECT` examples

This method gets the unencrypted secrets related to the job.


```sql
SELECT
jobName,
jobSecrets
FROM azure.data_box.jobs_credentials
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```