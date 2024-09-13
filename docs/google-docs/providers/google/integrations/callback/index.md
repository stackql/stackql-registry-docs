---
title: callback
hide_title: false
hide_table_of_contents: false
keywords:
  - callback
  - integrations
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

Creates, updates, deletes, gets or lists a <code>callback</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>callback</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.callback" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="callback_generate_token" /> | `EXEC` | <CopyableCode code="" /> | Receives the auth code and auth config id to combine that with the client id and secret to retrieve access tokens from the token endpoint. Returns either a success or error message when it's done. |
