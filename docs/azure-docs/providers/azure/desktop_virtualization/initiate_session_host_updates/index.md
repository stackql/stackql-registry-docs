---
title: initiate_session_host_updates
hide_title: false
hide_table_of_contents: false
keywords:
  - initiate_session_host_updates
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>initiate_session_host_updates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>initiate_session_host_updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.initiate_session_host_updates" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="post" /> | `EXEC` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Initiates a hostpool update or schedule an update for the future. |