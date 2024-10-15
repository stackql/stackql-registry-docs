---
title: servers_migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - servers_migrations
  - mysql
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

Creates, updates, deletes, gets or lists a <code>servers_migrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers_migrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.servers_migrations" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="cutover_migration" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Cutover migration for MySQL import, it will switch source elastic server DNS to flexible server. |
