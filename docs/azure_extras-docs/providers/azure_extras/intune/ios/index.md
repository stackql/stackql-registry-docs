---
title: ios
hide_title: false
hide_table_of_contents: false
keywords:
  - ios
  - intune
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

Creates, updates, deletes, gets or lists a <code>ios</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ios</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.intune.ios" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_app_for_mam_policy" /> | `EXEC` | <CopyableCode code="appName, hostName, policyName" /> | Add app to an iOSMAMPolicy. |
| <CopyableCode code="add_group_for_mam_policy" /> | `EXEC` | <CopyableCode code="groupId, hostName, policyName" /> | Add group to an iOSMAMPolicy. |
| <CopyableCode code="patch_mam_policy" /> | `EXEC` | <CopyableCode code="hostName, policyName" /> |  patch an iOSMAMPolicy. |
