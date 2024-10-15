---
title: runs_log_sas_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - runs_log_sas_urls
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>runs_log_sas_urls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runs_log_sas_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.runs_log_sas_urls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="logArtifactLink" /> | `string` | The link to logs in registry for a run on a azure container registry. |
| <CopyableCode code="logLink" /> | `string` | The link to logs for a run on a azure container registry. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, runId, subscriptionId" /> | Gets a link to download the run logs. |

## `SELECT` examples

Gets a link to download the run logs.


```sql
SELECT
logArtifactLink,
logLink
FROM azure.container_registry.runs_log_sas_urls
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runId = '{{ runId }}'
AND subscriptionId = '{{ subscriptionId }}';
```