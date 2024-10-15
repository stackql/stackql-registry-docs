---
title: locations_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_operation_results
  - network_admin
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

Creates, updates, deletes, gets or lists a <code>locations_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.network_admin.locations_operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation being performed on this particular object. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location" /> | Returns the list of operation results for a location |

## `SELECT` examples

Returns the list of operation results for a location


```sql
SELECT
name
FROM azure_stack.network_admin.locations_operation_results
WHERE location = '{{ location }}';
```