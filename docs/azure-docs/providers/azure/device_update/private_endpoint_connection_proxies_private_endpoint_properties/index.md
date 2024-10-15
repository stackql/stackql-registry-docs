---
title: private_endpoint_connection_proxies_private_endpoint_properties
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection_proxies_private_endpoint_properties
  - device_update
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

Creates, updates, deletes, gets or lists a <code>private_endpoint_connection_proxies_private_endpoint_properties</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_endpoint_connection_proxies_private_endpoint_properties</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_update.private_endpoint_connection_proxies_private_endpoint_properties" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) Updates a private endpoint inside the private endpoint connection proxy object. |
