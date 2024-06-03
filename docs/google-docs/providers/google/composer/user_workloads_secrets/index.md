---
title: user_workloads_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - user_workloads_secrets
  - composer
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_workloads_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.composer.user_workloads_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the Secret, in the form: "projects/&#123;projectId&#125;/locations/&#123;locationId&#125;/environments/&#123;environmentId&#125;/userWorkloadsSecrets/&#123;userWorkloadsSecretId&#125;" |
| <CopyableCode code="data" /> | `object` | Optional. The "data" field of Kubernetes Secret, organized in key-value pairs, which can contain sensitive values such as a password, a token, or a key. The values for all keys have to be base64-encoded strings. For details see: https://kubernetes.io/docs/concepts/configuration/secret/ |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentsId, locationsId, projectsId, userWorkloadsSecretsId" /> | Gets an existing user workloads Secret. Values of the "data" field in the response are cleared. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Lists user workloads Secrets. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Creates a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentsId, locationsId, projectsId, userWorkloadsSecretsId" /> | Deletes a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="environmentsId, locationsId, projectsId, userWorkloadsSecretsId" /> | Updates a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Lists user workloads Secrets. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
