---
title: email_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - email_registrations
  - data_share
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

Creates, updates, deletes, gets or lists a <code>email_registrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.email_registrations" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="activate_email" /> | `EXEC` | <CopyableCode code="location" /> | Activate the email registration for the current tenant |
| <CopyableCode code="register_email" /> | `EXEC` | <CopyableCode code="location" /> | Register an email for the current tenant |
