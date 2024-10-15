---
title: posts
hide_title: false
hide_table_of_contents: false
keywords:
  - posts
  - customer_lockbox
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

Creates, updates, deletes, gets or lists a <code>posts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>posts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.customer_lockbox.posts" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="disable_lockbox" /> | `EXEC` | <CopyableCode code="" /> | Disable Tenant for Lockbox  |
| <CopyableCode code="enable_lockbox" /> | `EXEC` | <CopyableCode code="" /> | Enable Tenant for Lockbox  |
