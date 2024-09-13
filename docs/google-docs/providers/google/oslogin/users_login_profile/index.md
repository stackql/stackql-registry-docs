---
title: users_login_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - users_login_profile
  - oslogin
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

Creates, updates, deletes, gets or lists a <code>users_login_profile</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users_login_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oslogin.users_login_profile" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. A unique user ID. |
| <CopyableCode code="posixAccounts" /> | `array` | The list of POSIX accounts associated with the user. |
| <CopyableCode code="sshPublicKeys" /> | `object` | A map from SSH public key fingerprint to the associated key object. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_login_profile" /> | `SELECT` | <CopyableCode code="usersId" /> | Retrieves the profile information used for logging in to a virtual machine on Google Compute Engine. |

## `SELECT` examples

Retrieves the profile information used for logging in to a virtual machine on Google Compute Engine.

```sql
SELECT
name,
posixAccounts,
sshPublicKeys
FROM google.oslogin.users_login_profile
WHERE usersId = '{{ usersId }}'; 
```
