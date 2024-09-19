---
title: relyingparty_project_config
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty_project_config
  - identitytoolkit
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

Creates, updates, deletes, gets or lists a <code>relyingparty_project_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relyingparty_project_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.identitytoolkit.relyingparty_project_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allowPasswordUser" /> | `boolean` | Whether to allow password user sign in or sign up. |
| <CopyableCode code="apiKey" /> | `string` | Browser API key, needed when making http request to Apiary. |
| <CopyableCode code="authorizedDomains" /> | `array` | Authorized domains. |
| <CopyableCode code="changeEmailTemplate" /> | `object` | Template for an email template. |
| <CopyableCode code="dynamicLinksDomain" /> | `string` |  |
| <CopyableCode code="enableAnonymousUser" /> | `boolean` | Whether anonymous user is enabled. |
| <CopyableCode code="idpConfig" /> | `array` | OAuth2 provider configuration. |
| <CopyableCode code="legacyResetPasswordTemplate" /> | `object` | Template for an email template. |
| <CopyableCode code="projectId" /> | `string` | Project ID of the relying party. |
| <CopyableCode code="resetPasswordTemplate" /> | `object` | Template for an email template. |
| <CopyableCode code="useEmailSending" /> | `boolean` | Whether to use email sending provided by Firebear. |
| <CopyableCode code="verifyEmailTemplate" /> | `object` | Template for an email template. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_project_config" /> | `SELECT` | <CopyableCode code="" /> | Get project configuration. |

## `SELECT` examples

Get project configuration.

```sql
SELECT
allowPasswordUser,
apiKey,
authorizedDomains,
changeEmailTemplate,
dynamicLinksDomain,
enableAnonymousUser,
idpConfig,
legacyResetPasswordTemplate,
projectId,
resetPasswordTemplate,
useEmailSending,
verifyEmailTemplate
FROM google.identitytoolkit.relyingparty_project_config
;
```
