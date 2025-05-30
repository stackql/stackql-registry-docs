---
title: event_threat_detection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - event_threat_detection_settings
  - securitycenter
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

Creates, updates, deletes, gets or lists a <code>event_threat_detection_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_threat_detection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.event_threat_detection_settings" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_event_threat_detection_settings_validate_custom_module" /> | `EXEC` | <CopyableCode code="foldersId" /> | Validates the given Event Threat Detection custom module. |
| <CopyableCode code="organizations_event_threat_detection_settings_validate_custom_module" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Validates the given Event Threat Detection custom module. |
| <CopyableCode code="projects_event_threat_detection_settings_validate_custom_module" /> | `EXEC` | <CopyableCode code="projectsId" /> | Validates the given Event Threat Detection custom module. |
