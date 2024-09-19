---
title: userinvitations
hide_title: false
hide_table_of_contents: false
keywords:
  - userinvitations
  - cloudidentity
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

Creates, updates, deletes, gets or lists a <code>userinvitations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>userinvitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.userinvitations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Shall be of the form `customers/{customer}/userinvitations/{user_email_address}`. |
| <CopyableCode code="mailsSentCount" /> | `string` | Number of invitation emails sent to the user. |
| <CopyableCode code="state" /> | `string` | State of the `UserInvitation`. |
| <CopyableCode code="updateTime" /> | `string` | Time when the `UserInvitation` was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customersId, userinvitationsId" /> | Retrieves a UserInvitation resource. **Note:** New consumer accounts with the customer's verified domain created within the previous 48 hours will not appear in the result. This delay also applies to newly-verified domains. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customersId" /> | Retrieves a list of UserInvitation resources. **Note:** New consumer accounts with the customer's verified domain created within the previous 48 hours will not appear in the result. This delay also applies to newly-verified domains. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="customersId, userinvitationsId" /> | Cancels a UserInvitation that was already sent. |
| <CopyableCode code="is_invitable_user" /> | `EXEC` | <CopyableCode code="customersId, userinvitationsId" /> | Verifies whether a user account is eligible to receive a UserInvitation (is an unmanaged account). Eligibility is based on the following criteria: * the email address is a consumer account and it's the primary email address of the account, and * the domain of the email address matches an existing verified Google Workspace or Cloud Identity domain If both conditions are met, the user is eligible. **Note:** This method is not supported for Workspace Essentials customers. |
| <CopyableCode code="send" /> | `EXEC` | <CopyableCode code="customersId, userinvitationsId" /> | Sends a UserInvitation to email. If the `UserInvitation` does not exist for this request and it is a valid request, the request creates a `UserInvitation`. **Note:** The `get` and `list` methods have a 48-hour delay where newly-created consumer accounts will not appear in the results. You can still send a `UserInvitation` to those accounts if you know the unmanaged email address and IsInvitableUser==True. |

## `SELECT` examples

Retrieves a list of UserInvitation resources. **Note:** New consumer accounts with the customer's verified domain created within the previous 48 hours will not appear in the result. This delay also applies to newly-verified domains.

```sql
SELECT
name,
mailsSentCount,
state,
updateTime
FROM google.cloudidentity.userinvitations
WHERE customersId = '{{ customersId }}';
```
