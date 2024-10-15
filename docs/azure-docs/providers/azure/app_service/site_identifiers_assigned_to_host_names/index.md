---
title: site_identifiers_assigned_to_host_names
hide_title: false
hide_table_of_contents: false
keywords:
  - site_identifiers_assigned_to_host_names
  - app_service
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

Creates, updates, deletes, gets or lists a <code>site_identifiers_assigned_to_host_names</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>site_identifiers_assigned_to_host_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.site_identifiers_assigned_to_host_names" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Identifier resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for List all apps that are assigned to a hostname. |

## `SELECT` examples

Description for List all apps that are assigned to a hostname.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.site_identifiers_assigned_to_host_names
WHERE subscriptionId = '{{ subscriptionId }}';
```