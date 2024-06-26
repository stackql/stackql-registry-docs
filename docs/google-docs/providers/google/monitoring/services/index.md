---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - monitoring
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.monitoring.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name for this Service. The format is: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]  |
| <CopyableCode code="appEngine" /> | `object` | App Engine service. Learn more at https://cloud.google.com/appengine. |
| <CopyableCode code="basicService" /> | `object` | A well-known service type, defined by its service type and service labels. Documentation and examples here (https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli). |
| <CopyableCode code="cloudEndpoints" /> | `object` | Cloud Endpoints service. Learn more at https://cloud.google.com/endpoints. |
| <CopyableCode code="cloudRun" /> | `object` | Cloud Run service. Learn more at https://cloud.google.com/run. |
| <CopyableCode code="clusterIstio" /> | `object` | Istio service scoped to a single Kubernetes cluster. Learn more at https://istio.io. Clusters running OSS Istio will have their services ingested as this type. |
| <CopyableCode code="custom" /> | `object` | Use a custom service to designate a service that you want to monitor when none of the other service types (like App Engine, Cloud Run, or a GKE type) matches your intended service. |
| <CopyableCode code="displayName" /> | `string` | Name used for UI elements listing this Service. |
| <CopyableCode code="gkeNamespace" /> | `object` | GKE Namespace. The field names correspond to the resource metadata labels on monitored resources that fall under a namespace (for example, k8s_container or k8s_pod). |
| <CopyableCode code="gkeService" /> | `object` | GKE Service. The "service" here represents a Kubernetes service object (https://kubernetes.io/docs/concepts/services-networking/service). The field names correspond to the resource labels on k8s_service monitored resources (https://cloud.google.com/monitoring/api/resources#tag_k8s_service). |
| <CopyableCode code="gkeWorkload" /> | `object` | A GKE Workload (Deployment, StatefulSet, etc). The field names correspond to the metadata labels on monitored resources that fall under a workload (for example, k8s_container or k8s_pod). |
| <CopyableCode code="istioCanonicalService" /> | `object` | Canonical service scoped to an Istio mesh. Anthos clusters running ASM &gt;= 1.6.8 will have their services ingested as this type. |
| <CopyableCode code="meshIstio" /> | `object` | Istio service scoped to an Istio mesh. Anthos clusters running ASM &lt; 1.6.8 will have their services ingested as this type. |
| <CopyableCode code="telemetry" /> | `object` | Configuration for how to query telemetry on a Service. |
| <CopyableCode code="userLabels" /> | `object` | Labels which have been used to annotate the service. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="services_list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | List Services for this Metrics Scope. |
| <CopyableCode code="services_create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Create a Service. |
| <CopyableCode code="_services_list" /> | `EXEC` | <CopyableCode code="parent, parentType" /> | List Services for this Metrics Scope. |
