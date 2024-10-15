---
title: products_details
hide_title: false
hide_table_of_contents: false
keywords:
  - products_details
  - azure_stack
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

Creates, updates, deletes, gets or lists a <code>products_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack.products_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="galleryPackageBlobSasUri" /> | `string` | The URI to the .azpkg file that provides information required for showing product in the gallery. |
| <CopyableCode code="productKind" /> | `string` | Specifies the kind of the product (virtualMachine or virtualMachineExtension). |
| <CopyableCode code="properties" /> | `object` | Product information. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="productName, registrationName, resourceGroup, subscriptionId" /> | Returns the extended properties of a product. |

## `SELECT` examples

Returns the extended properties of a product.


```sql
SELECT
galleryPackageBlobSasUri,
productKind,
properties
FROM azure_stack.azure_stack.products_details
WHERE productName = '{{ productName }}'
AND registrationName = '{{ registrationName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```