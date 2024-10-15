---
title: container_services
hide_title: false
hide_table_of_contents: false
keywords:
  - container_services
  - container_service_admin
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

Creates, updates, deletes, gets or lists a <code>container_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.container_service_admin.container_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Container service properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns a list of managed clusters present in all tenant location. |

## `SELECT` examples

Returns a list of managed clusters present in all tenant location.


```sql
SELECT
properties
FROM azure_stack.container_service_admin.container_services
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```