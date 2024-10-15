---
title: authorization_login_links
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_login_links
  - api_management
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

Creates, updates, deletes, gets or lists a <code>authorization_login_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorization_login_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.authorization_login_links" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="post" /> | `EXEC` | <CopyableCode code="authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Gets authorization login links. |
