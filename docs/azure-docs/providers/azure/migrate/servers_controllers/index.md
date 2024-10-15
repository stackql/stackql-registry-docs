---
title: servers_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers_controllers
  - migrate
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

Creates, updates, deletes, gets or lists a <code>servers_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.servers_controllers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Server REST resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_server_site_resource" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Get all machines in a site. |

## `SELECT` examples

Get all machines in a site.


```sql
SELECT
properties
FROM azure.migrate.servers_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```