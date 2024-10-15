---
title: data_plane_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - data_plane_applications
  - split
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

Creates, updates, deletes, gets or lists a <code>data_plane_applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_plane_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.split.data_plane_applications" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="exchange_token" /> | `EXEC` | <CopyableCode code="applicationId, resourceGroupName, subscriptionId, workspaceName, data__resource, data__token" /> | The action to exchange Split.IO data plane authentication token. |
