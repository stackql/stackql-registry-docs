---
title: configs
hide_title: false
hide_table_of_contents: false
keywords:
  - configs
  - apigateway
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
<tr><td><b>Name</b></td><td><code>configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigateway.configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the API Config. Format: projects/&#123;project&#125;/locations/global/apis/&#123;api&#125;/configs/&#123;api_config&#125; |
| <CopyableCode code="createTime" /> | `string` | Output only. Created time. |
| <CopyableCode code="displayName" /> | `string` | Optional. Display name. |
| <CopyableCode code="gatewayServiceAccount" /> | `string` | Immutable. The Google Cloud IAM Service Account that Gateways serving this config should use to authenticate to other services. This may either be the Service Account's email (`&#123;ACCOUNT_ID&#125;@&#123;PROJECT&#125;.iam.gserviceaccount.com`) or its full resource name (`projects/&#123;PROJECT&#125;/accounts/&#123;UNIQUE_ID&#125;`). This is most often used when the service is a GCP resource such as a Cloud Run Service or an IAP-secured service. |
| <CopyableCode code="grpcServices" /> | `array` | Optional. gRPC service definition files. If specified, openapi_documents must not be included. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| <CopyableCode code="managedServiceConfigs" /> | `array` | Optional. Service Configuration files. At least one must be included when using gRPC service definitions. See https://cloud.google.com/endpoints/docs/grpc/grpc-service-config#service_configuration_overview for the expected file contents. If multiple files are specified, the files are merged with the following rules: * All singular scalar fields are merged using "last one wins" semantics in the order of the files uploaded. * Repeated fields are concatenated. * Singular embedded messages are merged using these rules for nested fields. |
| <CopyableCode code="openapiDocuments" /> | `array` | Optional. OpenAPI specification documents. If specified, grpc_services and managed_service_configs must not be included. |
| <CopyableCode code="serviceConfigId" /> | `string` | Output only. The ID of the associated Service Config ( https://cloud.google.com/service-infrastructure/docs/glossary#config). |
| <CopyableCode code="state" /> | `string` | Output only. State of the API Config. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Updated time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apisId, configsId, locationsId, projectsId" /> | Gets details of a single ApiConfig. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId" /> | Lists ApiConfigs in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="apisId, locationsId, projectsId" /> | Creates a new ApiConfig in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apisId, configsId, locationsId, projectsId" /> | Deletes a single ApiConfig. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="apisId, locationsId, projectsId" /> | Lists ApiConfigs in a given project and location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="apisId, configsId, locationsId, projectsId" /> | Updates the parameters of a single ApiConfig. |
