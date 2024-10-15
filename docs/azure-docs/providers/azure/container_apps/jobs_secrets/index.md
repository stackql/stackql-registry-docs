---
title: jobs_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_secrets
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>jobs_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.jobs_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Secret Name. |
| <CopyableCode code="identity" /> | `string` | Resource ID of a managed identity to authenticate with Azure Key Vault, or System to use a system-assigned identity. |
| <CopyableCode code="keyVaultUrl" /> | `string` | Azure Key Vault URL pointing to the secret referenced by the container app. |
| <CopyableCode code="value" /> | `string` | Secret Value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
name,
identity,
keyVaultUrl,
value
FROM azure.container_apps.jobs_secrets
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```