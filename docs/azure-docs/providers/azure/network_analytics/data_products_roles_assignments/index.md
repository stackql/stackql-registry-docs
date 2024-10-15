---
title: data_products_roles_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - data_products_roles_assignments
  - network_analytics
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

Creates, updates, deletes, gets or lists a <code>data_products_roles_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_products_roles_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network_analytics.data_products_roles_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="count" /> | `integer` | Count of role assignments. |
| <CopyableCode code="roleAssignmentResponse" /> | `array` | list of role assignments |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId" /> | List user roles associated with the data product. |

## `SELECT` examples

List user roles associated with the data product.


```sql
SELECT
count,
roleAssignmentResponse
FROM azure.network_analytics.data_products_roles_assignments
WHERE dataProductName = '{{ dataProductName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```