---
title: acquisitions
hide_title: false
hide_table_of_contents: false
keywords:
  - acquisitions
  - storage_admin
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

Creates, updates, deletes, gets or lists a <code>acquisitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>acquisitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.storage_admin.acquisitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="acquisitionid" /> | `string` | The ID of page BLOB acquisition. |
| <CopyableCode code="blob" /> | `string` | The name of the page BLOB. |
| <CopyableCode code="container" /> | `string` | The container associated with the page BLOB. |
| <CopyableCode code="filePath" /> | `string` | The file path of the page BLOB file on storage cluster. |
| <CopyableCode code="filePathUnc" /> | `string` | The file path unc of the page BLOB file on storage cluster. |
| <CopyableCode code="maximumblobsize" /> | `integer` | The maximum size of the page BLOB. |
| <CopyableCode code="status" /> | `string` | The status of page BLOB acquisition. |
| <CopyableCode code="storageaccount" /> | `string` | The storage account that holds the page BLOB. |
| <CopyableCode code="susbcriptionid" /> | `string` | ID of the subscription associated with the page BLOB. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns a list of BLOB acquisitions. |

## `SELECT` examples

Returns a list of BLOB acquisitions.


```sql
SELECT
acquisitionid,
blob,
container,
filePath,
filePathUnc,
maximumblobsize,
status,
storageaccount,
susbcriptionid
FROM azure_stack.storage_admin.acquisitions
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```