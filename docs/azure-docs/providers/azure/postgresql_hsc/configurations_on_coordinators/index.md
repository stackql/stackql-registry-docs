---
title: configurations_on_coordinators
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations_on_coordinators
  - postgresql_hsc
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

Creates, updates, deletes, gets or lists a <code>configurations_on_coordinators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configurations_on_coordinators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_hsc.configurations_on_coordinators" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="clusterName, configurationName, resourceGroupName, subscriptionId" /> | Updates configuration of coordinator in a cluster |

## `REPLACE` example

Replaces all fields in the specified <code>configurations_on_coordinators</code> resource.

```sql
/*+ update */
REPLACE azure.postgresql_hsc.configurations_on_coordinators
SET 
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND configurationName = '{{ configurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
