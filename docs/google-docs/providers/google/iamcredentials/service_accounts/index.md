---
title: service_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - service_accounts
  - iamcredentials
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

Creates, updates, deletes, gets or lists a <code>service_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iamcredentials.service_accounts" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="generate_access_token" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | Generates an OAuth 2.0 access token for a service account. |
| <CopyableCode code="generate_id_token" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | Generates an OpenID Connect ID token for a service account. |
| <CopyableCode code="sign_blob" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | Signs a blob using a service account's system-managed private key. |
| <CopyableCode code="sign_jwt" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | Signs a JWT using a service account's system-managed private key. |
