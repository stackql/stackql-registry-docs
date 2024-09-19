---
title: registrations_authorization_code
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations_authorization_code
  - domains
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

Creates, updates, deletes, gets or lists a <code>registrations_authorization_code</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registrations_authorization_code</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.domains.registrations_authorization_code" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="code" /> | `string` | The Authorization Code in ASCII. It can be used to transfer the domain to or from another registrar. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="retrieve_authorization_code" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar. You can call this method only after 60 days have elapsed since the initial domain registration. Domains that have the `REQUIRE_PUSH_TRANSFER` property in the list of `domain_properties` don't support authorization codes and must use the `InitiatePushTransfer` method to initiate the process to transfer the domain to a different registrar. |

## `SELECT` examples

Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar. You can call this method only after 60 days have elapsed since the initial domain registration. Domains that have the `REQUIRE_PUSH_TRANSFER` property in the list of `domain_properties` don't support authorization codes and must use the `InitiatePushTransfer` method to initiate the process to transfer the domain to a different registrar.

```sql
SELECT
code
FROM google.domains.registrations_authorization_code
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND registrationsId = '{{ registrationsId }}';
```
