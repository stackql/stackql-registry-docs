---
title: replication_protected_items_appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protected_items_appliances
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_protected_items_appliances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_protected_items_appliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protected_items_appliances" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to update appliance of an ASR replication protected item. |
