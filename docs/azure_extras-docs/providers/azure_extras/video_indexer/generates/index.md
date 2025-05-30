---
title: generates
hide_title: false
hide_table_of_contents: false
keywords:
  - generates
  - video_indexer
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

Creates, updates, deletes, gets or lists a <code>generates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>generates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.video_indexer.generates" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="access_token" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__permissionType, data__scope" /> | Generate an Azure Video Indexer access token. |
| <CopyableCode code="restricted_viewer_access_token" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__scope" /> | Generate an Azure Video Indexer restricted viewer access token. |
