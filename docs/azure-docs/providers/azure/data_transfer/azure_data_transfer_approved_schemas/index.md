---
title: azure_data_transfer_approved_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_data_transfer_approved_schemas
  - data_transfer
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

Creates, updates, deletes, gets or lists a <code>azure_data_transfer_approved_schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_data_transfer_approved_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_transfer.azure_data_transfer_approved_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="value" /> | `array` | The schemas for this connection |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists approved schemas for Azure Data Transfer. |

## `SELECT` examples

Lists approved schemas for Azure Data Transfer.


```sql
SELECT
value
FROM azure.data_transfer.azure_data_transfer_approved_schemas
;
```