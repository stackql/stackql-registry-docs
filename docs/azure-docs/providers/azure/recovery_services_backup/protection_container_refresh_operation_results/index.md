---
title: protection_container_refresh_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_container_refresh_operation_results
  - recovery_services_backup
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

Creates, updates, deletes, gets or lists a <code>protection_container_refresh_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protection_container_refresh_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.protection_container_refresh_operation_results" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, operationId, resourceGroupName, subscriptionId, vaultName" /> | Provides the result of the refresh operation triggered by the BeginRefresh operation. |

## `SELECT` examples

Provides the result of the refresh operation triggered by the BeginRefresh operation.


```sql
SELECT

FROM azure.recovery_services_backup.protection_container_refresh_operation_results
WHERE fabricName = '{{ fabricName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```