---
title: catalogs_sync_error_details
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs_sync_error_details
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>catalogs_sync_error_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs_sync_error_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.catalogs_sync_error_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="conflicts" /> | `array` | Catalog items that have conflicting names. |
| <CopyableCode code="errors" /> | `array` | Errors that occured during synchronization. |
| <CopyableCode code="operationError" /> | `object` | Catalog error details |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId" /> | Gets catalog synchronization error details |

## `SELECT` examples

Gets catalog synchronization error details


```sql
SELECT
conflicts,
errors,
operationError
FROM azure.dev_center.catalogs_sync_error_details
WHERE catalogName = '{{ catalogName }}'
AND devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```