# Tool Use Cases and Prompt Library

This guide provides 10 prompt examples for every available tool in the Nutanix MCP Server, grouped by namespace.

## Namespace: `aiops`

### `aiops_scenarios_list`

Example prompts:

1. Use `aiops_scenarios_list` to list what-if scenarios.
2. Use `aiops_scenarios_list` to list what-if scenarios with `top: 10`.
3. Use `aiops_scenarios_list` to list what-if scenarios with `orderby: "name asc"`.
4. Use `aiops_scenarios_list` to list what-if scenarios with `orderby: "createdTime desc"`.
5. Use `aiops_scenarios_list` to list what-if scenarios with `filter: "name eq 'example'"`.
6. Use `aiops_scenarios_list` to list what-if scenarios with `filter: "contains(name, 'prod')"`.
7. Use `aiops_scenarios_list` to list what-if scenarios selecting fields with `select: "name,uuid"`.
8. Use `aiops_scenarios_list` to list what-if scenarios with pagination `skip: 50` and `top: 25`.
9. Use `aiops_scenarios_list` to list what-if scenarios and `expand` related entities.
10. Use `aiops_scenarios_list` to list what-if scenarios for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `aiops_vm_rightsizing_list`

Example prompts:

1. Use `aiops_vm_rightsizing_list` to get vm rightsizing recommendations.
2. Use `aiops_vm_rightsizing_list` to get vm rightsizing recommendations with `top: 10`.
3. Use `aiops_vm_rightsizing_list` to get vm rightsizing recommendations with `orderby: "name asc"`.
4. Use `aiops_vm_rightsizing_list` to get vm rightsizing recommendations with `orderby: "createdTime desc"`.
5. Use `aiops_vm_rightsizing_list` to get vm rightsizing recommendations with `filter: "name eq 'example'"`.
6. Use `aiops_vm_rightsizing_list` to get vm rightsizing recommendations with `filter: "contains(name, 'prod')"`.
7. Use `aiops_vm_rightsizing_list` to get vm rightsizing recommendations selecting fields with `select: "name,uuid"`.
8. Use `aiops_vm_rightsizing_list` to get vm rightsizing recommendations with pagination `skip: 50` and `top: 25`.
9. Use `aiops_vm_rightsizing_list` to get vm rightsizing recommendations and `expand` related entities.
10. Use `aiops_vm_rightsizing_list` to get vm rightsizing recommendations for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

## Namespace: `clustermgmt`

### `clustermgmt_clusters_list`

Example prompts:

1. Use `clustermgmt_clusters_list` to list clusters managed by prism central.
2. Use `clustermgmt_clusters_list` to list clusters managed by prism central with `top: 10`.
3. Use `clustermgmt_clusters_list` to list clusters managed by prism central with `orderby: "name asc"`.
4. Use `clustermgmt_clusters_list` to list clusters managed by prism central with `orderby: "createdTime desc"`.
5. Use `clustermgmt_clusters_list` to list clusters managed by prism central with `filter: "name eq 'example'"`.
6. Use `clustermgmt_clusters_list` to list clusters managed by prism central with `filter: "contains(name, 'prod')"`.
7. Use `clustermgmt_clusters_list` to list clusters managed by prism central selecting fields with `select: "name,uuid"`.
8. Use `clustermgmt_clusters_list` to list clusters managed by prism central with pagination `skip: 50` and `top: 25`.
9. Use `clustermgmt_clusters_list` to list clusters managed by prism central and `expand` related entities.
10. Use `clustermgmt_clusters_list` to list clusters managed by prism central for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `clustermgmt_cluster_get`

Example prompts:

1. Use `clustermgmt_cluster_get` to get cluster details by id for ID `<id>`.
2. Use `clustermgmt_cluster_get` with `select: "name,status"` to get cluster details by id for ID `<id>`.
3. Use `clustermgmt_cluster_get` with `expand` to get cluster details by id for ID `<id>`.
4. Use `clustermgmt_cluster_get` to get cluster details by id for ID `<id>` to validate configuration.
5. Use `clustermgmt_cluster_get` to get cluster details by id for ID `<id>` during troubleshooting.
6. Use `clustermgmt_cluster_get` to get cluster details by id for ID `<id>` after a change to confirm updates.
7. Use `clustermgmt_cluster_get` to get cluster details by id for ID `<id>` and verify metadata.
8. Use `clustermgmt_cluster_get` to get cluster details by id for ID `<id>` and capture key fields.
9. Use `clustermgmt_cluster_get` to get cluster details by id for ID `<id>` when auditing resources.
10. Use `clustermgmt_cluster_get` to get cluster details by id for ID `<id>` to confirm it exists.

### `clustermgmt_hosts_list`

Example prompts:

1. Use `clustermgmt_hosts_list` to list hosts across all clusters.
2. Use `clustermgmt_hosts_list` to list hosts across all clusters with `top: 10`.
3. Use `clustermgmt_hosts_list` to list hosts across all clusters with `orderby: "name asc"`.
4. Use `clustermgmt_hosts_list` to list hosts across all clusters with `orderby: "createdTime desc"`.
5. Use `clustermgmt_hosts_list` to list hosts across all clusters with `filter: "name eq 'example'"`.
6. Use `clustermgmt_hosts_list` to list hosts across all clusters with `filter: "contains(name, 'prod')"`.
7. Use `clustermgmt_hosts_list` to list hosts across all clusters selecting fields with `select: "name,uuid"`.
8. Use `clustermgmt_hosts_list` to list hosts across all clusters with pagination `skip: 50` and `top: 25`.
9. Use `clustermgmt_hosts_list` to list hosts across all clusters and `expand` related entities.
10. Use `clustermgmt_hosts_list` to list hosts across all clusters for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `clustermgmt_host_get`

Example prompts:

1. Use `clustermgmt_host_get` to get host details by id for ID `<id>`.
2. Use `clustermgmt_host_get` with `select: "name,status"` to get host details by id for ID `<id>`.
3. Use `clustermgmt_host_get` with `expand` to get host details by id for ID `<id>`.
4. Use `clustermgmt_host_get` to get host details by id for ID `<id>` to validate configuration.
5. Use `clustermgmt_host_get` to get host details by id for ID `<id>` during troubleshooting.
6. Use `clustermgmt_host_get` to get host details by id for ID `<id>` after a change to confirm updates.
7. Use `clustermgmt_host_get` to get host details by id for ID `<id>` and verify metadata.
8. Use `clustermgmt_host_get` to get host details by id for ID `<id>` and capture key fields.
9. Use `clustermgmt_host_get` to get host details by id for ID `<id>` when auditing resources.
10. Use `clustermgmt_host_get` to get host details by id for ID `<id>` to confirm it exists.

## Namespace: `datapolicies`

### `datapolicies_storage_policies_list`

Example prompts:

1. Use `datapolicies_storage_policies_list` to list storage policies.
2. Use `datapolicies_storage_policies_list` to list storage policies with `top: 10`.
3. Use `datapolicies_storage_policies_list` to list storage policies with `orderby: "name asc"`.
4. Use `datapolicies_storage_policies_list` to list storage policies with `orderby: "createdTime desc"`.
5. Use `datapolicies_storage_policies_list` to list storage policies with `filter: "name eq 'example'"`.
6. Use `datapolicies_storage_policies_list` to list storage policies with `filter: "contains(name, 'prod')"`.
7. Use `datapolicies_storage_policies_list` to list storage policies selecting fields with `select: "name,uuid"`.
8. Use `datapolicies_storage_policies_list` to list storage policies with pagination `skip: 50` and `top: 25`.
9. Use `datapolicies_storage_policies_list` to list storage policies and `expand` related entities.
10. Use `datapolicies_storage_policies_list` to list storage policies for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

## Namespace: `dataprotection`

### `dataprotection_policies_list`

Example prompts:

1. Use `dataprotection_policies_list` to list protection policies.
2. Use `dataprotection_policies_list` to list protection policies with `top: 10`.
3. Use `dataprotection_policies_list` to list protection policies with `orderby: "name asc"`.
4. Use `dataprotection_policies_list` to list protection policies with `orderby: "createdTime desc"`.
5. Use `dataprotection_policies_list` to list protection policies with `filter: "name eq 'example'"`.
6. Use `dataprotection_policies_list` to list protection policies with `filter: "contains(name, 'prod')"`.
7. Use `dataprotection_policies_list` to list protection policies selecting fields with `select: "name,uuid"`.
8. Use `dataprotection_policies_list` to list protection policies with pagination `skip: 50` and `top: 25`.
9. Use `dataprotection_policies_list` to list protection policies and `expand` related entities.
10. Use `dataprotection_policies_list` to list protection policies for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `dataprotection_policy_get`

Example prompts:

1. Use `dataprotection_policy_get` to get protection policy details by id for ID `<id>`.
2. Use `dataprotection_policy_get` with `select: "name,status"` to get protection policy details by id for ID `<id>`.
3. Use `dataprotection_policy_get` with `expand` to get protection policy details by id for ID `<id>`.
4. Use `dataprotection_policy_get` to get protection policy details by id for ID `<id>` to validate configuration.
5. Use `dataprotection_policy_get` to get protection policy details by id for ID `<id>` during troubleshooting.
6. Use `dataprotection_policy_get` to get protection policy details by id for ID `<id>` after a change to confirm updates.
7. Use `dataprotection_policy_get` to get protection policy details by id for ID `<id>` and verify metadata.
8. Use `dataprotection_policy_get` to get protection policy details by id for ID `<id>` and capture key fields.
9. Use `dataprotection_policy_get` to get protection policy details by id for ID `<id>` when auditing resources.
10. Use `dataprotection_policy_get` to get protection policy details by id for ID `<id>` to confirm it exists.

### `dataprotection_recovery_points_list`

Example prompts:

1. Use `dataprotection_recovery_points_list` to list recovery points (snapshots).
2. Use `dataprotection_recovery_points_list` to list recovery points (snapshots) with `top: 10`.
3. Use `dataprotection_recovery_points_list` to list recovery points (snapshots) with `orderby: "name asc"`.
4. Use `dataprotection_recovery_points_list` to list recovery points (snapshots) with `orderby: "createdTime desc"`.
5. Use `dataprotection_recovery_points_list` to list recovery points (snapshots) with `filter: "name eq 'example'"`.
6. Use `dataprotection_recovery_points_list` to list recovery points (snapshots) with `filter: "contains(name, 'prod')"`.
7. Use `dataprotection_recovery_points_list` to list recovery points (snapshots) selecting fields with `select: "name,uuid"`.
8. Use `dataprotection_recovery_points_list` to list recovery points (snapshots) with pagination `skip: 50` and `top: 25`.
9. Use `dataprotection_recovery_points_list` to list recovery points (snapshots) and `expand` related entities.
10. Use `dataprotection_recovery_points_list` to list recovery points (snapshots) for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `dataprotection_recovery_point_get`

Example prompts:

1. Use `dataprotection_recovery_point_get` to get recovery point details by id for ID `<id>`.
2. Use `dataprotection_recovery_point_get` with `select: "name,status"` to get recovery point details by id for ID `<id>`.
3. Use `dataprotection_recovery_point_get` with `expand` to get recovery point details by id for ID `<id>`.
4. Use `dataprotection_recovery_point_get` to get recovery point details by id for ID `<id>` to validate configuration.
5. Use `dataprotection_recovery_point_get` to get recovery point details by id for ID `<id>` during troubleshooting.
6. Use `dataprotection_recovery_point_get` to get recovery point details by id for ID `<id>` after a change to confirm updates.
7. Use `dataprotection_recovery_point_get` to get recovery point details by id for ID `<id>` and verify metadata.
8. Use `dataprotection_recovery_point_get` to get recovery point details by id for ID `<id>` and capture key fields.
9. Use `dataprotection_recovery_point_get` to get recovery point details by id for ID `<id>` when auditing resources.
10. Use `dataprotection_recovery_point_get` to get recovery point details by id for ID `<id>` to confirm it exists.

## Namespace: `files`

### `files_servers_list`

Example prompts:

1. Use `files_servers_list` to list file servers.
2. Use `files_servers_list` to list file servers with `top: 10`.
3. Use `files_servers_list` to list file servers with `orderby: "name asc"`.
4. Use `files_servers_list` to list file servers with `orderby: "createdTime desc"`.
5. Use `files_servers_list` to list file servers with `filter: "name eq 'example'"`.
6. Use `files_servers_list` to list file servers with `filter: "contains(name, 'prod')"`.
7. Use `files_servers_list` to list file servers selecting fields with `select: "name,uuid"`.
8. Use `files_servers_list` to list file servers with pagination `skip: 50` and `top: 25`.
9. Use `files_servers_list` to list file servers and `expand` related entities.
10. Use `files_servers_list` to list file servers for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `files_server_get`

Example prompts:

1. Use `files_server_get` to get file server details by id for ID `<id>`.
2. Use `files_server_get` with `select: "name,status"` to get file server details by id for ID `<id>`.
3. Use `files_server_get` with `expand` to get file server details by id for ID `<id>`.
4. Use `files_server_get` to get file server details by id for ID `<id>` to validate configuration.
5. Use `files_server_get` to get file server details by id for ID `<id>` during troubleshooting.
6. Use `files_server_get` to get file server details by id for ID `<id>` after a change to confirm updates.
7. Use `files_server_get` to get file server details by id for ID `<id>` and verify metadata.
8. Use `files_server_get` to get file server details by id for ID `<id>` and capture key fields.
9. Use `files_server_get` to get file server details by id for ID `<id>` when auditing resources.
10. Use `files_server_get` to get file server details by id for ID `<id>` to confirm it exists.

### `files_shares_list`

Example prompts:

1. Use `files_shares_list` to list file shares/mount targets.
2. Use `files_shares_list` to list file shares/mount targets with `top: 10`.
3. Use `files_shares_list` to list file shares/mount targets with `orderby: "name asc"`.
4. Use `files_shares_list` to list file shares/mount targets with `orderby: "createdTime desc"`.
5. Use `files_shares_list` to list file shares/mount targets with `filter: "name eq 'example'"`.
6. Use `files_shares_list` to list file shares/mount targets with `filter: "contains(name, 'prod')"`.
7. Use `files_shares_list` to list file shares/mount targets selecting fields with `select: "name,uuid"`.
8. Use `files_shares_list` to list file shares/mount targets with pagination `skip: 50` and `top: 25`.
9. Use `files_shares_list` to list file shares/mount targets and `expand` related entities.
10. Use `files_shares_list` to list file shares/mount targets for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

## Namespace: `iam`

### `iam_users_list`

Example prompts:

1. Use `iam_users_list` to list users.
2. Use `iam_users_list` to list users with `top: 10`.
3. Use `iam_users_list` to list users with `orderby: "name asc"`.
4. Use `iam_users_list` to list users with `orderby: "createdTime desc"`.
5. Use `iam_users_list` to list users with `filter: "name eq 'example'"`.
6. Use `iam_users_list` to list users with `filter: "contains(name, 'prod')"`.
7. Use `iam_users_list` to list users selecting fields with `select: "name,uuid"`.
8. Use `iam_users_list` to list users with pagination `skip: 50` and `top: 25`.
9. Use `iam_users_list` to list users and `expand` related entities.
10. Use `iam_users_list` to list users for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `iam_user_get`

Example prompts:

1. Use `iam_user_get` to get user details by id for ID `<id>`.
2. Use `iam_user_get` with `select: "name,status"` to get user details by id for ID `<id>`.
3. Use `iam_user_get` with `expand` to get user details by id for ID `<id>`.
4. Use `iam_user_get` to get user details by id for ID `<id>` to validate configuration.
5. Use `iam_user_get` to get user details by id for ID `<id>` during troubleshooting.
6. Use `iam_user_get` to get user details by id for ID `<id>` after a change to confirm updates.
7. Use `iam_user_get` to get user details by id for ID `<id>` and verify metadata.
8. Use `iam_user_get` to get user details by id for ID `<id>` and capture key fields.
9. Use `iam_user_get` to get user details by id for ID `<id>` when auditing resources.
10. Use `iam_user_get` to get user details by id for ID `<id>` to confirm it exists.

### `iam_roles_list`

Example prompts:

1. Use `iam_roles_list` to list roles.
2. Use `iam_roles_list` to list roles with `top: 10`.
3. Use `iam_roles_list` to list roles with `orderby: "name asc"`.
4. Use `iam_roles_list` to list roles with `orderby: "createdTime desc"`.
5. Use `iam_roles_list` to list roles with `filter: "name eq 'example'"`.
6. Use `iam_roles_list` to list roles with `filter: "contains(name, 'prod')"`.
7. Use `iam_roles_list` to list roles selecting fields with `select: "name,uuid"`.
8. Use `iam_roles_list` to list roles with pagination `skip: 50` and `top: 25`.
9. Use `iam_roles_list` to list roles and `expand` related entities.
10. Use `iam_roles_list` to list roles for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `iam_role_get`

Example prompts:

1. Use `iam_role_get` to get role details by id for ID `<id>`.
2. Use `iam_role_get` with `select: "name,status"` to get role details by id for ID `<id>`.
3. Use `iam_role_get` with `expand` to get role details by id for ID `<id>`.
4. Use `iam_role_get` to get role details by id for ID `<id>` to validate configuration.
5. Use `iam_role_get` to get role details by id for ID `<id>` during troubleshooting.
6. Use `iam_role_get` to get role details by id for ID `<id>` after a change to confirm updates.
7. Use `iam_role_get` to get role details by id for ID `<id>` and verify metadata.
8. Use `iam_role_get` to get role details by id for ID `<id>` and capture key fields.
9. Use `iam_role_get` to get role details by id for ID `<id>` when auditing resources.
10. Use `iam_role_get` to get role details by id for ID `<id>` to confirm it exists.

### `iam_directory_services_list`

Example prompts:

1. Use `iam_directory_services_list` to list directory services (ad, ldap).
2. Use `iam_directory_services_list` to list directory services (ad, ldap) with `top: 10`.
3. Use `iam_directory_services_list` to list directory services (ad, ldap) with `orderby: "name asc"`.
4. Use `iam_directory_services_list` to list directory services (ad, ldap) with `orderby: "createdTime desc"`.
5. Use `iam_directory_services_list` to list directory services (ad, ldap) with `filter: "name eq 'example'"`.
6. Use `iam_directory_services_list` to list directory services (ad, ldap) with `filter: "contains(name, 'prod')"`.
7. Use `iam_directory_services_list` to list directory services (ad, ldap) selecting fields with `select: "name,uuid"`.
8. Use `iam_directory_services_list` to list directory services (ad, ldap) with pagination `skip: 50` and `top: 25`.
9. Use `iam_directory_services_list` to list directory services (ad, ldap) and `expand` related entities.
10. Use `iam_directory_services_list` to list directory services (ad, ldap) for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

## Namespace: `licensing`

### `licensing_summary_get`

Example prompts:

1. Use `licensing_summary_get` to get licensing summary and compliance status.
2. Use `licensing_summary_get` to get licensing summary and compliance status for a compliance review.
3. Use `licensing_summary_get` to get licensing summary and compliance status before a planned change.
4. Use `licensing_summary_get` to get licensing summary and compliance status to validate environment posture.
5. Use `licensing_summary_get` to get licensing summary and compliance status when compiling audit evidence.
6. Use `licensing_summary_get` to get licensing summary and compliance status and share the summary with stakeholders.
7. Use `licensing_summary_get` to get licensing summary and compliance status for a periodic health check.
8. Use `licensing_summary_get` to get licensing summary and compliance status and compare to last week's output.
9. Use `licensing_summary_get` to get licensing summary and compliance status to detect drift.
10. Use `licensing_summary_get` to get licensing summary and compliance status and log the results in a report.

### `licensing_allowances_list`

Example prompts:

1. Use `licensing_allowances_list` to list license allowances/entitlements.
2. Use `licensing_allowances_list` to list license allowances/entitlements with `top: 10`.
3. Use `licensing_allowances_list` to list license allowances/entitlements with `orderby: "name asc"`.
4. Use `licensing_allowances_list` to list license allowances/entitlements with `orderby: "createdTime desc"`.
5. Use `licensing_allowances_list` to list license allowances/entitlements with `filter: "name eq 'example'"`.
6. Use `licensing_allowances_list` to list license allowances/entitlements with `filter: "contains(name, 'prod')"`.
7. Use `licensing_allowances_list` to list license allowances/entitlements selecting fields with `select: "name,uuid"`.
8. Use `licensing_allowances_list` to list license allowances/entitlements with pagination `skip: 50` and `top: 25`.
9. Use `licensing_allowances_list` to list license allowances/entitlements and `expand` related entities.
10. Use `licensing_allowances_list` to list license allowances/entitlements for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

## Namespace: `lifecycle`

### `lifecycle_entities_list`

Example prompts:

1. Use `lifecycle_entities_list` to list lcm entities (software/firmware).
2. Use `lifecycle_entities_list` to list lcm entities (software/firmware) with `top: 10`.
3. Use `lifecycle_entities_list` to list lcm entities (software/firmware) with `orderby: "name asc"`.
4. Use `lifecycle_entities_list` to list lcm entities (software/firmware) with `orderby: "createdTime desc"`.
5. Use `lifecycle_entities_list` to list lcm entities (software/firmware) with `filter: "name eq 'example'"`.
6. Use `lifecycle_entities_list` to list lcm entities (software/firmware) with `filter: "contains(name, 'prod')"`.
7. Use `lifecycle_entities_list` to list lcm entities (software/firmware) selecting fields with `select: "name,uuid"`.
8. Use `lifecycle_entities_list` to list lcm entities (software/firmware) with pagination `skip: 50` and `top: 25`.
9. Use `lifecycle_entities_list` to list lcm entities (software/firmware) and `expand` related entities.
10. Use `lifecycle_entities_list` to list lcm entities (software/firmware) for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `lifecycle_recommendations_get`

Example prompts:

1. Use `lifecycle_recommendations_get` to get update recommendations.
2. Use `lifecycle_recommendations_get` to get update recommendations with `top: 10`.
3. Use `lifecycle_recommendations_get` to get update recommendations with `orderby: "name asc"`.
4. Use `lifecycle_recommendations_get` to get update recommendations with `orderby: "createdTime desc"`.
5. Use `lifecycle_recommendations_get` to get update recommendations with `filter: "name eq 'example'"`.
6. Use `lifecycle_recommendations_get` to get update recommendations with `filter: "contains(name, 'prod')"`.
7. Use `lifecycle_recommendations_get` to get update recommendations selecting fields with `select: "name,uuid"`.
8. Use `lifecycle_recommendations_get` to get update recommendations with pagination `skip: 50` and `top: 25`.
9. Use `lifecycle_recommendations_get` to get update recommendations and `expand` related entities.
10. Use `lifecycle_recommendations_get` to get update recommendations for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

## Namespace: `microseg`

### `microseg_policies_list`

Example prompts:

1. Use `microseg_policies_list` to list network security policies.
2. Use `microseg_policies_list` to list network security policies with `top: 10`.
3. Use `microseg_policies_list` to list network security policies with `orderby: "name asc"`.
4. Use `microseg_policies_list` to list network security policies with `orderby: "createdTime desc"`.
5. Use `microseg_policies_list` to list network security policies with `filter: "name eq 'example'"`.
6. Use `microseg_policies_list` to list network security policies with `filter: "contains(name, 'prod')"`.
7. Use `microseg_policies_list` to list network security policies selecting fields with `select: "name,uuid"`.
8. Use `microseg_policies_list` to list network security policies with pagination `skip: 50` and `top: 25`.
9. Use `microseg_policies_list` to list network security policies and `expand` related entities.
10. Use `microseg_policies_list` to list network security policies for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `microseg_policy_get`

Example prompts:

1. Use `microseg_policy_get` to get security policy details by id for ID `<id>`.
2. Use `microseg_policy_get` with `select: "name,status"` to get security policy details by id for ID `<id>`.
3. Use `microseg_policy_get` with `expand` to get security policy details by id for ID `<id>`.
4. Use `microseg_policy_get` to get security policy details by id for ID `<id>` to validate configuration.
5. Use `microseg_policy_get` to get security policy details by id for ID `<id>` during troubleshooting.
6. Use `microseg_policy_get` to get security policy details by id for ID `<id>` after a change to confirm updates.
7. Use `microseg_policy_get` to get security policy details by id for ID `<id>` and verify metadata.
8. Use `microseg_policy_get` to get security policy details by id for ID `<id>` and capture key fields.
9. Use `microseg_policy_get` to get security policy details by id for ID `<id>` when auditing resources.
10. Use `microseg_policy_get` to get security policy details by id for ID `<id>` to confirm it exists.

### `microseg_address_groups_list`

Example prompts:

1. Use `microseg_address_groups_list` to list address groups.
2. Use `microseg_address_groups_list` to list address groups with `top: 10`.
3. Use `microseg_address_groups_list` to list address groups with `orderby: "name asc"`.
4. Use `microseg_address_groups_list` to list address groups with `orderby: "createdTime desc"`.
5. Use `microseg_address_groups_list` to list address groups with `filter: "name eq 'example'"`.
6. Use `microseg_address_groups_list` to list address groups with `filter: "contains(name, 'prod')"`.
7. Use `microseg_address_groups_list` to list address groups selecting fields with `select: "name,uuid"`.
8. Use `microseg_address_groups_list` to list address groups with pagination `skip: 50` and `top: 25`.
9. Use `microseg_address_groups_list` to list address groups and `expand` related entities.
10. Use `microseg_address_groups_list` to list address groups for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `microseg_service_groups_list`

Example prompts:

1. Use `microseg_service_groups_list` to list service groups.
2. Use `microseg_service_groups_list` to list service groups with `top: 10`.
3. Use `microseg_service_groups_list` to list service groups with `orderby: "name asc"`.
4. Use `microseg_service_groups_list` to list service groups with `orderby: "createdTime desc"`.
5. Use `microseg_service_groups_list` to list service groups with `filter: "name eq 'example'"`.
6. Use `microseg_service_groups_list` to list service groups with `filter: "contains(name, 'prod')"`.
7. Use `microseg_service_groups_list` to list service groups selecting fields with `select: "name,uuid"`.
8. Use `microseg_service_groups_list` to list service groups with pagination `skip: 50` and `top: 25`.
9. Use `microseg_service_groups_list` to list service groups and `expand` related entities.
10. Use `microseg_service_groups_list` to list service groups for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

## Namespace: `monitoring`

### `monitoring_alerts_list`

Example prompts:

1. Use `monitoring_alerts_list` to list alerts.
2. Use `monitoring_alerts_list` to list alerts with `top: 10`.
3. Use `monitoring_alerts_list` to list alerts with `orderby: "name asc"`.
4. Use `monitoring_alerts_list` to list alerts with `orderby: "createdTime desc"`.
5. Use `monitoring_alerts_list` to list alerts with `filter: "name eq 'example'"`.
6. Use `monitoring_alerts_list` to list alerts with `filter: "contains(name, 'prod')"`.
7. Use `monitoring_alerts_list` to list alerts selecting fields with `select: "name,uuid"`.
8. Use `monitoring_alerts_list` to list alerts with pagination `skip: 50` and `top: 25`.
9. Use `monitoring_alerts_list` to list alerts and `expand` related entities.
10. Use `monitoring_alerts_list` to list alerts for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `monitoring_alert_get`

Example prompts:

1. Use `monitoring_alert_get` to get alert details by id for ID `<id>`.
2. Use `monitoring_alert_get` with `select: "name,status"` to get alert details by id for ID `<id>`.
3. Use `monitoring_alert_get` with `expand` to get alert details by id for ID `<id>`.
4. Use `monitoring_alert_get` to get alert details by id for ID `<id>` to validate configuration.
5. Use `monitoring_alert_get` to get alert details by id for ID `<id>` during troubleshooting.
6. Use `monitoring_alert_get` to get alert details by id for ID `<id>` after a change to confirm updates.
7. Use `monitoring_alert_get` to get alert details by id for ID `<id>` and verify metadata.
8. Use `monitoring_alert_get` to get alert details by id for ID `<id>` and capture key fields.
9. Use `monitoring_alert_get` to get alert details by id for ID `<id>` when auditing resources.
10. Use `monitoring_alert_get` to get alert details by id for ID `<id>` to confirm it exists.

### `monitoring_alert_acknowledge`

Example prompts:

1. Use `monitoring_alert_acknowledge` to acknowledge an alert for ID `<id>`.
2. Use `monitoring_alert_acknowledge` to acknowledge an alert for ID `<id>` during maintenance.
3. Use `monitoring_alert_acknowledge` to acknowledge an alert for ID `<id>` as part of a runbook.
4. Use `monitoring_alert_acknowledge` to acknowledge an alert for ID `<id>` after confirming approvals.
5. Use `monitoring_alert_acknowledge` to acknowledge an alert for ID `<id>` and monitor the task status.
6. Use `monitoring_alert_acknowledge` to acknowledge an alert for ID `<id>` in a scheduled change.
7. Use `monitoring_alert_acknowledge` to acknowledge an alert for ID `<id>` when testing automation.
8. Use `monitoring_alert_acknowledge` to acknowledge an alert for ID `<id>` after verifying prerequisites.
9. Use `monitoring_alert_acknowledge` to acknowledge an alert for ID `<id>` and verify state changes.
10. Use `monitoring_alert_acknowledge` to acknowledge an alert for ID `<id>` and log the outcome.

### `monitoring_alert_resolve`

Example prompts:

1. Use `monitoring_alert_resolve` to resolve an alert for ID `<id>`.
2. Use `monitoring_alert_resolve` to resolve an alert for ID `<id>` during maintenance.
3. Use `monitoring_alert_resolve` to resolve an alert for ID `<id>` as part of a runbook.
4. Use `monitoring_alert_resolve` to resolve an alert for ID `<id>` after confirming approvals.
5. Use `monitoring_alert_resolve` to resolve an alert for ID `<id>` and monitor the task status.
6. Use `monitoring_alert_resolve` to resolve an alert for ID `<id>` in a scheduled change.
7. Use `monitoring_alert_resolve` to resolve an alert for ID `<id>` when testing automation.
8. Use `monitoring_alert_resolve` to resolve an alert for ID `<id>` after verifying prerequisites.
9. Use `monitoring_alert_resolve` to resolve an alert for ID `<id>` and verify state changes.
10. Use `monitoring_alert_resolve` to resolve an alert for ID `<id>` and log the outcome.

### `monitoring_events_list`

Example prompts:

1. Use `monitoring_events_list` to list events.
2. Use `monitoring_events_list` to list events with `top: 10`.
3. Use `monitoring_events_list` to list events with `orderby: "name asc"`.
4. Use `monitoring_events_list` to list events with `orderby: "createdTime desc"`.
5. Use `monitoring_events_list` to list events with `filter: "name eq 'example'"`.
6. Use `monitoring_events_list` to list events with `filter: "contains(name, 'prod')"`.
7. Use `monitoring_events_list` to list events selecting fields with `select: "name,uuid"`.
8. Use `monitoring_events_list` to list events with pagination `skip: 50` and `top: 25`.
9. Use `monitoring_events_list` to list events and `expand` related entities.
10. Use `monitoring_events_list` to list events for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `monitoring_audits_list`

Example prompts:

1. Use `monitoring_audits_list` to list audit logs.
2. Use `monitoring_audits_list` to list audit logs with `top: 10`.
3. Use `monitoring_audits_list` to list audit logs with `orderby: "name asc"`.
4. Use `monitoring_audits_list` to list audit logs with `orderby: "createdTime desc"`.
5. Use `monitoring_audits_list` to list audit logs with `filter: "name eq 'example'"`.
6. Use `monitoring_audits_list` to list audit logs with `filter: "contains(name, 'prod')"`.
7. Use `monitoring_audits_list` to list audit logs selecting fields with `select: "name,uuid"`.
8. Use `monitoring_audits_list` to list audit logs with pagination `skip: 50` and `top: 25`.
9. Use `monitoring_audits_list` to list audit logs and `expand` related entities.
10. Use `monitoring_audits_list` to list audit logs for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

## Namespace: `networking`

### `networking_subnets_list`

Example prompts:

1. Use `networking_subnets_list` to list subnets/networks.
2. Use `networking_subnets_list` to list subnets/networks with `top: 10`.
3. Use `networking_subnets_list` to list subnets/networks with `orderby: "name asc"`.
4. Use `networking_subnets_list` to list subnets/networks with `orderby: "createdTime desc"`.
5. Use `networking_subnets_list` to list subnets/networks with `filter: "name eq 'example'"`.
6. Use `networking_subnets_list` to list subnets/networks with `filter: "contains(name, 'prod')"`.
7. Use `networking_subnets_list` to list subnets/networks selecting fields with `select: "name,uuid"`.
8. Use `networking_subnets_list` to list subnets/networks with pagination `skip: 50` and `top: 25`.
9. Use `networking_subnets_list` to list subnets/networks and `expand` related entities.
10. Use `networking_subnets_list` to list subnets/networks for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `networking_subnet_get`

Example prompts:

1. Use `networking_subnet_get` to get subnet details by id for ID `<id>`.
2. Use `networking_subnet_get` with `select: "name,status"` to get subnet details by id for ID `<id>`.
3. Use `networking_subnet_get` with `expand` to get subnet details by id for ID `<id>`.
4. Use `networking_subnet_get` to get subnet details by id for ID `<id>` to validate configuration.
5. Use `networking_subnet_get` to get subnet details by id for ID `<id>` during troubleshooting.
6. Use `networking_subnet_get` to get subnet details by id for ID `<id>` after a change to confirm updates.
7. Use `networking_subnet_get` to get subnet details by id for ID `<id>` and verify metadata.
8. Use `networking_subnet_get` to get subnet details by id for ID `<id>` and capture key fields.
9. Use `networking_subnet_get` to get subnet details by id for ID `<id>` when auditing resources.
10. Use `networking_subnet_get` to get subnet details by id for ID `<id>` to confirm it exists.

### `networking_subnet_create`

Example prompts:

1. Use `networking_subnet_create` to create a new subnet named `example-01`.
2. Use `networking_subnet_create` to create a new subnet with required IDs and a descriptive name.
3. Use `networking_subnet_create` to create a new subnet sized for a small test workload.
4. Use `networking_subnet_create` to create a new subnet sized for a production workload.
5. Use `networking_subnet_create` to create a new subnet and attach it to a specific cluster.
6. Use `networking_subnet_create` to create a new subnet with networking set to the target subnet.
7. Use `networking_subnet_create` to create a new subnet and specify storage size or image references.
8. Use `networking_subnet_create` to create a new subnet with a standard naming convention.
9. Use `networking_subnet_create` to create a new subnet as part of a migration plan.
10. Use `networking_subnet_create` to create a new subnet and record the returned task ID.

### `networking_subnet_delete`

Example prompts:

1. Use `networking_subnet_delete` to delete a subnet with ID `<id>`.
2. Use `networking_subnet_delete` to delete a subnet after confirming backups for ID `<id>`.
3. Use `networking_subnet_delete` to delete a subnet for a decommissioned resource ID `<id>`.
4. Use `networking_subnet_delete` to delete a subnet and then verify tasks for ID `<id>`.
5. Use `networking_subnet_delete` to delete a subnet during cleanup of test assets ID `<id>`.
6. Use `networking_subnet_delete` to delete a subnet to free capacity for ID `<id>`.
7. Use `networking_subnet_delete` to delete a subnet when retiring a workload ID `<id>`.
8. Use `networking_subnet_delete` to delete a subnet with a change window for ID `<id>`.
9. Use `networking_subnet_delete` to delete a subnet and document the removal of ID `<id>`.
10. Use `networking_subnet_delete` to delete a subnet after validating dependency checks for ID `<id>`.

### `networking_vpcs_list`

Example prompts:

1. Use `networking_vpcs_list` to list virtual private clouds.
2. Use `networking_vpcs_list` to list virtual private clouds with `top: 10`.
3. Use `networking_vpcs_list` to list virtual private clouds with `orderby: "name asc"`.
4. Use `networking_vpcs_list` to list virtual private clouds with `orderby: "createdTime desc"`.
5. Use `networking_vpcs_list` to list virtual private clouds with `filter: "name eq 'example'"`.
6. Use `networking_vpcs_list` to list virtual private clouds with `filter: "contains(name, 'prod')"`.
7. Use `networking_vpcs_list` to list virtual private clouds selecting fields with `select: "name,uuid"`.
8. Use `networking_vpcs_list` to list virtual private clouds with pagination `skip: 50` and `top: 25`.
9. Use `networking_vpcs_list` to list virtual private clouds and `expand` related entities.
10. Use `networking_vpcs_list` to list virtual private clouds for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `networking_floating_ips_list`

Example prompts:

1. Use `networking_floating_ips_list` to list floating ips.
2. Use `networking_floating_ips_list` to list floating ips with `top: 10`.
3. Use `networking_floating_ips_list` to list floating ips with `orderby: "name asc"`.
4. Use `networking_floating_ips_list` to list floating ips with `orderby: "createdTime desc"`.
5. Use `networking_floating_ips_list` to list floating ips with `filter: "name eq 'example'"`.
6. Use `networking_floating_ips_list` to list floating ips with `filter: "contains(name, 'prod')"`.
7. Use `networking_floating_ips_list` to list floating ips selecting fields with `select: "name,uuid"`.
8. Use `networking_floating_ips_list` to list floating ips with pagination `skip: 50` and `top: 25`.
9. Use `networking_floating_ips_list` to list floating ips and `expand` related entities.
10. Use `networking_floating_ips_list` to list floating ips for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

## Namespace: `objects`

### `objects_stores_list`

Example prompts:

1. Use `objects_stores_list` to list object stores.
2. Use `objects_stores_list` to list object stores with `top: 10`.
3. Use `objects_stores_list` to list object stores with `orderby: "name asc"`.
4. Use `objects_stores_list` to list object stores with `orderby: "createdTime desc"`.
5. Use `objects_stores_list` to list object stores with `filter: "name eq 'example'"`.
6. Use `objects_stores_list` to list object stores with `filter: "contains(name, 'prod')"`.
7. Use `objects_stores_list` to list object stores selecting fields with `select: "name,uuid"`.
8. Use `objects_stores_list` to list object stores with pagination `skip: 50` and `top: 25`.
9. Use `objects_stores_list` to list object stores and `expand` related entities.
10. Use `objects_stores_list` to list object stores for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `objects_store_get`

Example prompts:

1. Use `objects_store_get` to get object store details by id for ID `<id>`.
2. Use `objects_store_get` with `select: "name,status"` to get object store details by id for ID `<id>`.
3. Use `objects_store_get` with `expand` to get object store details by id for ID `<id>`.
4. Use `objects_store_get` to get object store details by id for ID `<id>` to validate configuration.
5. Use `objects_store_get` to get object store details by id for ID `<id>` during troubleshooting.
6. Use `objects_store_get` to get object store details by id for ID `<id>` after a change to confirm updates.
7. Use `objects_store_get` to get object store details by id for ID `<id>` and verify metadata.
8. Use `objects_store_get` to get object store details by id for ID `<id>` and capture key fields.
9. Use `objects_store_get` to get object store details by id for ID `<id>` when auditing resources.
10. Use `objects_store_get` to get object store details by id for ID `<id>` to confirm it exists.

## Namespace: `opsmgmt`

### `opsmgmt_reports_list`

Example prompts:

1. Use `opsmgmt_reports_list` to list reports.
2. Use `opsmgmt_reports_list` to list reports with `top: 10`.
3. Use `opsmgmt_reports_list` to list reports with `orderby: "name asc"`.
4. Use `opsmgmt_reports_list` to list reports with `orderby: "createdTime desc"`.
5. Use `opsmgmt_reports_list` to list reports with `filter: "name eq 'example'"`.
6. Use `opsmgmt_reports_list` to list reports with `filter: "contains(name, 'prod')"`.
7. Use `opsmgmt_reports_list` to list reports selecting fields with `select: "name,uuid"`.
8. Use `opsmgmt_reports_list` to list reports with pagination `skip: 50` and `top: 25`.
9. Use `opsmgmt_reports_list` to list reports and `expand` related entities.
10. Use `opsmgmt_reports_list` to list reports for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `opsmgmt_report_get`

Example prompts:

1. Use `opsmgmt_report_get` to get report details by id for ID `<id>`.
2. Use `opsmgmt_report_get` with `select: "name,status"` to get report details by id for ID `<id>`.
3. Use `opsmgmt_report_get` with `expand` to get report details by id for ID `<id>`.
4. Use `opsmgmt_report_get` to get report details by id for ID `<id>` to validate configuration.
5. Use `opsmgmt_report_get` to get report details by id for ID `<id>` during troubleshooting.
6. Use `opsmgmt_report_get` to get report details by id for ID `<id>` after a change to confirm updates.
7. Use `opsmgmt_report_get` to get report details by id for ID `<id>` and verify metadata.
8. Use `opsmgmt_report_get` to get report details by id for ID `<id>` and capture key fields.
9. Use `opsmgmt_report_get` to get report details by id for ID `<id>` when auditing resources.
10. Use `opsmgmt_report_get` to get report details by id for ID `<id>` to confirm it exists.

## Namespace: `prism`

### `prism_tasks_list`

Example prompts:

1. Use `prism_tasks_list` to list tasks.
2. Use `prism_tasks_list` to list tasks with `top: 10`.
3. Use `prism_tasks_list` to list tasks with `orderby: "name asc"`.
4. Use `prism_tasks_list` to list tasks with `orderby: "createdTime desc"`.
5. Use `prism_tasks_list` to list tasks with `filter: "name eq 'example'"`.
6. Use `prism_tasks_list` to list tasks with `filter: "contains(name, 'prod')"`.
7. Use `prism_tasks_list` to list tasks selecting fields with `select: "name,uuid"`.
8. Use `prism_tasks_list` to list tasks with pagination `skip: 50` and `top: 25`.
9. Use `prism_tasks_list` to list tasks and `expand` related entities.
10. Use `prism_tasks_list` to list tasks for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `prism_task_get`

Example prompts:

1. Use `prism_task_get` to get task status by id for ID `<id>`.
2. Use `prism_task_get` with `select: "name,status"` to get task status by id for ID `<id>`.
3. Use `prism_task_get` with `expand` to get task status by id for ID `<id>`.
4. Use `prism_task_get` to get task status by id for ID `<id>` to validate configuration.
5. Use `prism_task_get` to get task status by id for ID `<id>` during troubleshooting.
6. Use `prism_task_get` to get task status by id for ID `<id>` after a change to confirm updates.
7. Use `prism_task_get` to get task status by id for ID `<id>` and verify metadata.
8. Use `prism_task_get` to get task status by id for ID `<id>` and capture key fields.
9. Use `prism_task_get` to get task status by id for ID `<id>` when auditing resources.
10. Use `prism_task_get` to get task status by id for ID `<id>` to confirm it exists.

### `prism_categories_list`

Example prompts:

1. Use `prism_categories_list` to list categories.
2. Use `prism_categories_list` to list categories with `top: 10`.
3. Use `prism_categories_list` to list categories with `orderby: "name asc"`.
4. Use `prism_categories_list` to list categories with `orderby: "createdTime desc"`.
5. Use `prism_categories_list` to list categories with `filter: "name eq 'example'"`.
6. Use `prism_categories_list` to list categories with `filter: "contains(name, 'prod')"`.
7. Use `prism_categories_list` to list categories selecting fields with `select: "name,uuid"`.
8. Use `prism_categories_list` to list categories with pagination `skip: 50` and `top: 25`.
9. Use `prism_categories_list` to list categories and `expand` related entities.
10. Use `prism_categories_list` to list categories for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `prism_category_get`

Example prompts:

1. Use `prism_category_get` to get category details by key for ID `<id>`.
2. Use `prism_category_get` with `select: "name,status"` to get category details by key for ID `<id>`.
3. Use `prism_category_get` with `expand` to get category details by key for ID `<id>`.
4. Use `prism_category_get` to get category details by key for ID `<id>` to validate configuration.
5. Use `prism_category_get` to get category details by key for ID `<id>` during troubleshooting.
6. Use `prism_category_get` to get category details by key for ID `<id>` after a change to confirm updates.
7. Use `prism_category_get` to get category details by key for ID `<id>` and verify metadata.
8. Use `prism_category_get` to get category details by key for ID `<id>` and capture key fields.
9. Use `prism_category_get` to get category details by key for ID `<id>` when auditing resources.
10. Use `prism_category_get` to get category details by key for ID `<id>` to confirm it exists.

## Namespace: `security`

### `security_config_get`

Example prompts:

1. Use `security_config_get` to get security configuration.
2. Use `security_config_get` to get security configuration for a compliance review.
3. Use `security_config_get` to get security configuration before a planned change.
4. Use `security_config_get` to get security configuration to validate environment posture.
5. Use `security_config_get` to get security configuration when compiling audit evidence.
6. Use `security_config_get` to get security configuration and share the summary with stakeholders.
7. Use `security_config_get` to get security configuration for a periodic health check.
8. Use `security_config_get` to get security configuration and compare to last week's output.
9. Use `security_config_get` to get security configuration to detect drift.
10. Use `security_config_get` to get security configuration and log the results in a report.

## Namespace: `storage`

### `storage_containers_list`

Example prompts:

1. Use `storage_containers_list` to list storage containers.
2. Use `storage_containers_list` to list storage containers with `top: 10`.
3. Use `storage_containers_list` to list storage containers with `orderby: "name asc"`.
4. Use `storage_containers_list` to list storage containers with `orderby: "createdTime desc"`.
5. Use `storage_containers_list` to list storage containers with `filter: "name eq 'example'"`.
6. Use `storage_containers_list` to list storage containers with `filter: "contains(name, 'prod')"`.
7. Use `storage_containers_list` to list storage containers selecting fields with `select: "name,uuid"`.
8. Use `storage_containers_list` to list storage containers with pagination `skip: 50` and `top: 25`.
9. Use `storage_containers_list` to list storage containers and `expand` related entities.
10. Use `storage_containers_list` to list storage containers for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `storage_container_get`

Example prompts:

1. Use `storage_container_get` to get storage container details by id for ID `<id>`.
2. Use `storage_container_get` with `select: "name,status"` to get storage container details by id for ID `<id>`.
3. Use `storage_container_get` with `expand` to get storage container details by id for ID `<id>`.
4. Use `storage_container_get` to get storage container details by id for ID `<id>` to validate configuration.
5. Use `storage_container_get` to get storage container details by id for ID `<id>` during troubleshooting.
6. Use `storage_container_get` to get storage container details by id for ID `<id>` after a change to confirm updates.
7. Use `storage_container_get` to get storage container details by id for ID `<id>` and verify metadata.
8. Use `storage_container_get` to get storage container details by id for ID `<id>` and capture key fields.
9. Use `storage_container_get` to get storage container details by id for ID `<id>` when auditing resources.
10. Use `storage_container_get` to get storage container details by id for ID `<id>` to confirm it exists.

## Namespace: `vmm`

### `vmm_list`

Example prompts:

1. Use `vmm_list` to list virtual machines in prism central.
2. Use `vmm_list` to list virtual machines in prism central with `top: 10`.
3. Use `vmm_list` to list virtual machines in prism central with `orderby: "name asc"`.
4. Use `vmm_list` to list virtual machines in prism central with `orderby: "createdTime desc"`.
5. Use `vmm_list` to list virtual machines in prism central with `filter: "name eq 'example'"`.
6. Use `vmm_list` to list virtual machines in prism central with `filter: "contains(name, 'prod')"`.
7. Use `vmm_list` to list virtual machines in prism central selecting fields with `select: "name,uuid"`.
8. Use `vmm_list` to list virtual machines in prism central with pagination `skip: 50` and `top: 25`.
9. Use `vmm_list` to list virtual machines in prism central and `expand` related entities.
10. Use `vmm_list` to list virtual machines in prism central for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `vmm_get`

Example prompts:

1. Use `vmm_get` to get virtual machine details by id for ID `<id>`.
2. Use `vmm_get` with `select: "name,status"` to get virtual machine details by id for ID `<id>`.
3. Use `vmm_get` with `expand` to get virtual machine details by id for ID `<id>`.
4. Use `vmm_get` to get virtual machine details by id for ID `<id>` to validate configuration.
5. Use `vmm_get` to get virtual machine details by id for ID `<id>` during troubleshooting.
6. Use `vmm_get` to get virtual machine details by id for ID `<id>` after a change to confirm updates.
7. Use `vmm_get` to get virtual machine details by id for ID `<id>` and verify metadata.
8. Use `vmm_get` to get virtual machine details by id for ID `<id>` and capture key fields.
9. Use `vmm_get` to get virtual machine details by id for ID `<id>` when auditing resources.
10. Use `vmm_get` to get virtual machine details by id for ID `<id>` to confirm it exists.

### `vmm_create`

Example prompts:

1. Use `vmm_create` to create a new virtual machine named `example-01`.
2. Use `vmm_create` to create a new virtual machine with required IDs and a descriptive name.
3. Use `vmm_create` to create a new virtual machine sized for a small test workload.
4. Use `vmm_create` to create a new virtual machine sized for a production workload.
5. Use `vmm_create` to create a new virtual machine and attach it to a specific cluster.
6. Use `vmm_create` to create a new virtual machine with networking set to the target subnet.
7. Use `vmm_create` to create a new virtual machine and specify storage size or image references.
8. Use `vmm_create` to create a new virtual machine with a standard naming convention.
9. Use `vmm_create` to create a new virtual machine as part of a migration plan.
10. Use `vmm_create` to create a new virtual machine and record the returned task ID.

### `vmm_delete`

Example prompts:

1. Use `vmm_delete` to delete a virtual machine with ID `<id>`.
2. Use `vmm_delete` to delete a virtual machine after confirming backups for ID `<id>`.
3. Use `vmm_delete` to delete a virtual machine for a decommissioned resource ID `<id>`.
4. Use `vmm_delete` to delete a virtual machine and then verify tasks for ID `<id>`.
5. Use `vmm_delete` to delete a virtual machine during cleanup of test assets ID `<id>`.
6. Use `vmm_delete` to delete a virtual machine to free capacity for ID `<id>`.
7. Use `vmm_delete` to delete a virtual machine when retiring a workload ID `<id>`.
8. Use `vmm_delete` to delete a virtual machine with a change window for ID `<id>`.
9. Use `vmm_delete` to delete a virtual machine and document the removal of ID `<id>`.
10. Use `vmm_delete` to delete a virtual machine after validating dependency checks for ID `<id>`.

### `vmm_power_on`

Example prompts:

1. Use `vmm_power_on` to power on a virtual machine for ID `<id>`.
2. Use `vmm_power_on` to power on a virtual machine for ID `<id>` during maintenance.
3. Use `vmm_power_on` to power on a virtual machine for ID `<id>` as part of a runbook.
4. Use `vmm_power_on` to power on a virtual machine for ID `<id>` after confirming approvals.
5. Use `vmm_power_on` to power on a virtual machine for ID `<id>` and monitor the task status.
6. Use `vmm_power_on` to power on a virtual machine for ID `<id>` in a scheduled change.
7. Use `vmm_power_on` to power on a virtual machine for ID `<id>` when testing automation.
8. Use `vmm_power_on` to power on a virtual machine for ID `<id>` after verifying prerequisites.
9. Use `vmm_power_on` to power on a virtual machine for ID `<id>` and verify state changes.
10. Use `vmm_power_on` to power on a virtual machine for ID `<id>` and log the outcome.

### `vmm_power_off`

Example prompts:

1. Use `vmm_power_off` to power off a virtual machine for ID `<id>`.
2. Use `vmm_power_off` to power off a virtual machine for ID `<id>` during maintenance.
3. Use `vmm_power_off` to power off a virtual machine for ID `<id>` as part of a runbook.
4. Use `vmm_power_off` to power off a virtual machine for ID `<id>` after confirming approvals.
5. Use `vmm_power_off` to power off a virtual machine for ID `<id>` and monitor the task status.
6. Use `vmm_power_off` to power off a virtual machine for ID `<id>` in a scheduled change.
7. Use `vmm_power_off` to power off a virtual machine for ID `<id>` when testing automation.
8. Use `vmm_power_off` to power off a virtual machine for ID `<id>` after verifying prerequisites.
9. Use `vmm_power_off` to power off a virtual machine for ID `<id>` and verify state changes.
10. Use `vmm_power_off` to power off a virtual machine for ID `<id>` and log the outcome.

### `vmm_reset`

Example prompts:

1. Use `vmm_reset` to reset (hard reboot) a virtual machine for ID `<id>`.
2. Use `vmm_reset` to reset (hard reboot) a virtual machine for ID `<id>` during maintenance.
3. Use `vmm_reset` to reset (hard reboot) a virtual machine for ID `<id>` as part of a runbook.
4. Use `vmm_reset` to reset (hard reboot) a virtual machine for ID `<id>` after confirming approvals.
5. Use `vmm_reset` to reset (hard reboot) a virtual machine for ID `<id>` and monitor the task status.
6. Use `vmm_reset` to reset (hard reboot) a virtual machine for ID `<id>` in a scheduled change.
7. Use `vmm_reset` to reset (hard reboot) a virtual machine for ID `<id>` when testing automation.
8. Use `vmm_reset` to reset (hard reboot) a virtual machine for ID `<id>` after verifying prerequisites.
9. Use `vmm_reset` to reset (hard reboot) a virtual machine for ID `<id>` and verify state changes.
10. Use `vmm_reset` to reset (hard reboot) a virtual machine for ID `<id>` and log the outcome.

### `vmm_guest_shutdown`

Example prompts:

1. Use `vmm_guest_shutdown` to gracefully shutdown a vm via guest tools for ID `<id>`.
2. Use `vmm_guest_shutdown` to gracefully shutdown a vm via guest tools for ID `<id>` during maintenance.
3. Use `vmm_guest_shutdown` to gracefully shutdown a vm via guest tools for ID `<id>` as part of a runbook.
4. Use `vmm_guest_shutdown` to gracefully shutdown a vm via guest tools for ID `<id>` after confirming approvals.
5. Use `vmm_guest_shutdown` to gracefully shutdown a vm via guest tools for ID `<id>` and monitor the task status.
6. Use `vmm_guest_shutdown` to gracefully shutdown a vm via guest tools for ID `<id>` in a scheduled change.
7. Use `vmm_guest_shutdown` to gracefully shutdown a vm via guest tools for ID `<id>` when testing automation.
8. Use `vmm_guest_shutdown` to gracefully shutdown a vm via guest tools for ID `<id>` after verifying prerequisites.
9. Use `vmm_guest_shutdown` to gracefully shutdown a vm via guest tools for ID `<id>` and verify state changes.
10. Use `vmm_guest_shutdown` to gracefully shutdown a vm via guest tools for ID `<id>` and log the outcome.

### `vmm_guest_reboot`

Example prompts:

1. Use `vmm_guest_reboot` to gracefully reboot a vm via guest tools for ID `<id>`.
2. Use `vmm_guest_reboot` to gracefully reboot a vm via guest tools for ID `<id>` during maintenance.
3. Use `vmm_guest_reboot` to gracefully reboot a vm via guest tools for ID `<id>` as part of a runbook.
4. Use `vmm_guest_reboot` to gracefully reboot a vm via guest tools for ID `<id>` after confirming approvals.
5. Use `vmm_guest_reboot` to gracefully reboot a vm via guest tools for ID `<id>` and monitor the task status.
6. Use `vmm_guest_reboot` to gracefully reboot a vm via guest tools for ID `<id>` in a scheduled change.
7. Use `vmm_guest_reboot` to gracefully reboot a vm via guest tools for ID `<id>` when testing automation.
8. Use `vmm_guest_reboot` to gracefully reboot a vm via guest tools for ID `<id>` after verifying prerequisites.
9. Use `vmm_guest_reboot` to gracefully reboot a vm via guest tools for ID `<id>` and verify state changes.
10. Use `vmm_guest_reboot` to gracefully reboot a vm via guest tools for ID `<id>` and log the outcome.

### `vmm_images_list`

Example prompts:

1. Use `vmm_images_list` to list disk images in prism central.
2. Use `vmm_images_list` to list disk images in prism central with `top: 10`.
3. Use `vmm_images_list` to list disk images in prism central with `orderby: "name asc"`.
4. Use `vmm_images_list` to list disk images in prism central with `orderby: "createdTime desc"`.
5. Use `vmm_images_list` to list disk images in prism central with `filter: "name eq 'example'"`.
6. Use `vmm_images_list` to list disk images in prism central with `filter: "contains(name, 'prod')"`.
7. Use `vmm_images_list` to list disk images in prism central selecting fields with `select: "name,uuid"`.
8. Use `vmm_images_list` to list disk images in prism central with pagination `skip: 50` and `top: 25`.
9. Use `vmm_images_list` to list disk images in prism central and `expand` related entities.
10. Use `vmm_images_list` to list disk images in prism central for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `vmm_image_get`

Example prompts:

1. Use `vmm_image_get` to get image details by id for ID `<id>`.
2. Use `vmm_image_get` with `select: "name,status"` to get image details by id for ID `<id>`.
3. Use `vmm_image_get` with `expand` to get image details by id for ID `<id>`.
4. Use `vmm_image_get` to get image details by id for ID `<id>` to validate configuration.
5. Use `vmm_image_get` to get image details by id for ID `<id>` during troubleshooting.
6. Use `vmm_image_get` to get image details by id for ID `<id>` after a change to confirm updates.
7. Use `vmm_image_get` to get image details by id for ID `<id>` and verify metadata.
8. Use `vmm_image_get` to get image details by id for ID `<id>` and capture key fields.
9. Use `vmm_image_get` to get image details by id for ID `<id>` when auditing resources.
10. Use `vmm_image_get` to get image details by id for ID `<id>` to confirm it exists.

## Namespace: `volumes`

### `volumes_groups_list`

Example prompts:

1. Use `volumes_groups_list` to list volume groups.
2. Use `volumes_groups_list` to list volume groups with `top: 10`.
3. Use `volumes_groups_list` to list volume groups with `orderby: "name asc"`.
4. Use `volumes_groups_list` to list volume groups with `orderby: "createdTime desc"`.
5. Use `volumes_groups_list` to list volume groups with `filter: "name eq 'example'"`.
6. Use `volumes_groups_list` to list volume groups with `filter: "contains(name, 'prod')"`.
7. Use `volumes_groups_list` to list volume groups selecting fields with `select: "name,uuid"`.
8. Use `volumes_groups_list` to list volume groups with pagination `skip: 50` and `top: 25`.
9. Use `volumes_groups_list` to list volume groups and `expand` related entities.
10. Use `volumes_groups_list` to list volume groups for a specific timeframe using `filter: "createdTime gt 2024-01-01T00:00:00Z"`.

### `volumes_group_get`

Example prompts:

1. Use `volumes_group_get` to get volume group details by id for ID `<id>`.
2. Use `volumes_group_get` with `select: "name,status"` to get volume group details by id for ID `<id>`.
3. Use `volumes_group_get` with `expand` to get volume group details by id for ID `<id>`.
4. Use `volumes_group_get` to get volume group details by id for ID `<id>` to validate configuration.
5. Use `volumes_group_get` to get volume group details by id for ID `<id>` during troubleshooting.
6. Use `volumes_group_get` to get volume group details by id for ID `<id>` after a change to confirm updates.
7. Use `volumes_group_get` to get volume group details by id for ID `<id>` and verify metadata.
8. Use `volumes_group_get` to get volume group details by id for ID `<id>` and capture key fields.
9. Use `volumes_group_get` to get volume group details by id for ID `<id>` when auditing resources.
10. Use `volumes_group_get` to get volume group details by id for ID `<id>` to confirm it exists.

### `volumes_group_create`

Example prompts:

1. Use `volumes_group_create` to create a new volume group named `example-01`.
2. Use `volumes_group_create` to create a new volume group with required IDs and a descriptive name.
3. Use `volumes_group_create` to create a new volume group sized for a small test workload.
4. Use `volumes_group_create` to create a new volume group sized for a production workload.
5. Use `volumes_group_create` to create a new volume group and attach it to a specific cluster.
6. Use `volumes_group_create` to create a new volume group with networking set to the target subnet.
7. Use `volumes_group_create` to create a new volume group and specify storage size or image references.
8. Use `volumes_group_create` to create a new volume group with a standard naming convention.
9. Use `volumes_group_create` to create a new volume group as part of a migration plan.
10. Use `volumes_group_create` to create a new volume group and record the returned task ID.

### `volumes_group_delete`

Example prompts:

1. Use `volumes_group_delete` to delete a volume group with ID `<id>`.
2. Use `volumes_group_delete` to delete a volume group after confirming backups for ID `<id>`.
3. Use `volumes_group_delete` to delete a volume group for a decommissioned resource ID `<id>`.
4. Use `volumes_group_delete` to delete a volume group and then verify tasks for ID `<id>`.
5. Use `volumes_group_delete` to delete a volume group during cleanup of test assets ID `<id>`.
6. Use `volumes_group_delete` to delete a volume group to free capacity for ID `<id>`.
7. Use `volumes_group_delete` to delete a volume group when retiring a workload ID `<id>`.
8. Use `volumes_group_delete` to delete a volume group with a change window for ID `<id>`.
9. Use `volumes_group_delete` to delete a volume group and document the removal of ID `<id>`.
10. Use `volumes_group_delete` to delete a volume group after validating dependency checks for ID `<id>`.

## Complex Workflows (Chaining Multiple Tools)

These examples show how to chain multiple tools together to complete common workflows.

### Provision a new VM from an image

- Use `clustermgmt_clusters_list` to identify the target cluster.
- Use `networking_subnets_list` to choose the destination subnet.
- Use `vmm_images_list` to find the desired image.
- Use `vmm_create` to create the VM with the selected cluster, subnet, and image.
- Use `prism_tasks_list` or `prism_task_get` to monitor the create task.

Details:

- Validate the cluster has enough capacity and matches the intended environment (prod/test).
- Confirm the subnet provides the correct IP range and gateway for the workload.
- Pick an image that matches the OS and version required for the VM build.
- Capture the task ID from `vmm_create` for downstream monitoring and auditing.
- Track task completion, then optionally follow up with `vmm_get` to verify the final VM state.

### Investigate and resolve a critical alert

- Use `monitoring_alerts_list` with a severity filter to find critical alerts.
- Use `monitoring_alert_get` to inspect the alert details.
- Use `monitoring_events_list` to correlate related events.
- Use `monitoring_alert_acknowledge` to acknowledge the alert.
- Use `monitoring_alert_resolve` once remediation is complete.

Details:

- Start with a filter like `severity eq 'CRITICAL'` to focus on urgent alerts.
- Pull the alert metadata (impact, timestamps, affected entities) to build a timeline.
- Correlate events to identify root-cause signals versus downstream symptoms.
- Acknowledge to signal ownership while remediation is underway.
- Resolve only after confirming the issue is cleared and the system is stable.

### Decommission a VM safely

- Use `vmm_get` to verify the VM state and metadata.
- Use `dataprotection_recovery_points_list` to confirm recent recovery points.
- Use `vmm_power_off` or `vmm_guest_shutdown` to stop the VM.
- Use `vmm_delete` to delete the VM.
- Use `prism_task_get` to confirm deletion completion.

Details:

- Confirm the VM is not running critical workloads and record its identifiers.
- Verify a recent recovery point exists if rollback is required.
- Use guest shutdown when possible to avoid data loss.
- Document the delete task ID to track completion and auditing.
- Validate the VM no longer appears in inventory after task completion.

### Create and validate a subnet for a new environment

- Use `clustermgmt_clusters_list` to select the cluster.
- Use `networking_subnet_create` to create the new subnet.
- Use `networking_subnets_list` to verify the subnet appears in inventory.
- Use `networking_subnet_get` to confirm subnet configuration details.
- Use `prism_tasks_list` to watch any background tasks.

Details:

- Select the cluster that will host workloads for the new environment.
- Provide VLAN/overlay details, gateway, and prefix length for correct routing.
- Confirm the subnet shows up in the inventory list.
- Validate critical fields (VLAN ID, gateway, prefix) after creation.
- Ensure any provisioning tasks complete before attaching workloads.

### Apply microsegmentation review

- Use `microseg_policies_list` to inventory policies.
- Use `microseg_policy_get` to review a policy's rules.
- Use `microseg_address_groups_list` to validate address group membership.
- Use `microseg_service_groups_list` to confirm service group definitions.
- Use `prism_tasks_list` to track any follow-up actions.

Details:

- Enumerate policies to understand existing segmentation posture.
- Inspect rule precedence, directionality, and enforcement modes.
- Validate address groups map to the intended subnets or workloads.
- Confirm service groups reflect approved ports and protocols.
- Track any changes for audit evidence and operational visibility.

### Review licensing compliance

- Use `licensing_summary_get` to capture current compliance status.
- Use `licensing_allowances_list` to review entitlements.
- Use `iam_users_list` to compare active users against allowances.
- Use `opsmgmt_reports_list` to pull recent compliance reports.
- Use `opsmgmt_report_get` to review a specific report output.

Details:

- Capture the compliance summary as a baseline snapshot.
- Compare allowances with actual utilization to detect overages.
- Cross-check active users and roles to ensure alignment with licensing.
- Review recent reports for historical trends and anomalies.
- Archive the report output for audit readiness.

### Plan right-sizing for VMs

- Use `aiops_vm_rightsizing_list` to gather recommendations.
- Use `vmm_list` to map recommendations to active VMs.
- Use `vmm_get` to confirm current sizing details.
- Use `monitoring_events_list` to check recent performance events.
- Use `prism_tasks_list` to monitor any resulting change tasks.

Details:

- Capture recommended CPU/memory changes and affected VMs.
- Map each recommendation to current VM inventory for validation.
- Confirm the current configuration before planning a change.
- Review performance events to verify if recommendations align with usage.
- Track any resizing tasks through completion for operational confirmation.

### Investigate storage capacity

- Use `storage_containers_list` to see container capacity.
- Use `storage_container_get` to drill into a specific container.
- Use `volumes_groups_list` to understand attached volume groups.
- Use `volumes_group_get` to inspect a volume group detail.
- Use `datapolicies_storage_policies_list` to review policy assignments.

Details:

- Identify containers nearing capacity thresholds.
- Drill into a container to review usage, efficiency, and alerts.
- See which volume groups are consuming space within the container.
- Inspect volume group metadata (size, attachments, policies).
- Validate storage policies to ensure they match performance needs.

### Audit identity and access

- Use `iam_users_list` to list all users.
- Use `iam_user_get` to review a specific user's profile.
- Use `iam_roles_list` to list role definitions.
- Use `iam_role_get` to inspect a role's permissions.
- Use `iam_directory_services_list` to verify directory integrations.

Details:

- Capture a user inventory for baseline access review.
- Confirm individual users' status, source, and assigned roles.
- Review roles for least-privilege alignment.
- Validate that role permissions match approved access patterns.
- Ensure directory integrations are healthy and up to date.

### Check lifecycle update readiness

- Use `lifecycle_entities_list` to list managed entities.
- Use `lifecycle_recommendations_get` to see recommended updates.
- Use `clustermgmt_hosts_list` to confirm host inventory.
- Use `monitoring_alerts_list` to ensure no blocking alerts exist.
- Use `prism_tasks_list` to monitor any LCM tasks.

Details:

- Confirm all managed entities are present and accounted for.
- Review recommendations to understand scope and impact.
- Verify host inventory is current before initiating updates.
- Ensure no critical alerts would block maintenance windows.
- Track LCM tasks for progress and final completion status.
